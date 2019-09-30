import asyncio

from aiohttp import web
import aiohttp_jinja2
from demo import db


@aiohttp_jinja2.template('index.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.posts.select())
        records = await cursor.fetchall()
        posts_res = [dict(p) for p in records]
        return {"posts_res": posts_res}


@aiohttp_jinja2.template('detail.html')
async def comments_detail(request):
    async with request.app['db'].acquire() as conn:
        post_id = request.match_info['post_id']
        try:
            posts, comments = await db.get_posts(conn, post_id)
        except db.RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))
        return {
            'posts': posts,
            'comments': comments
        }


async def vote(request):
    async with request.app['db'].acquire() as conn:  # коннектимся к бд
        post_id = int(request.match_info['post_id'])
        data = await request.post()
        try:
            comment_id = int(data['vote'])
        except (KeyError, TypeError, ValueError) as e:
            raise web.HTTPBadRequest(
                text='You have not specified comment value') from e
        try:
            await db.vote(conn, post_id, comment_id)
        except db.RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))
        router = request.app.router
        url = router['results'].url_for(post_id=str(post_id))
        return web.HTTPFound(location=url)


@aiohttp_jinja2.template('result.html')
async def results(request):
    async with request.app['db'].acquire() as conn:
        post_id = request.match_info['post_id']
        try:
            posts, comments = await db.get_posts(conn, post_id)
        except db.RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))
        return {
            'posts': posts,
            'comments': comments
        }
