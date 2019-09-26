from aiohttp import web
from sqlalchemy import select
from aiohttp_jinja2 import template
from .. import db

@template('index.html')
async def index(request):
    site_name = request.app['config'].get('site_name')
    return {'site_name':site_name}

async def post(request):
    async with request.app['db'].acquire() as conn:
        query = select([db.post])#если отдные entries [db.post.c.id, db.post.c.title]
        print(query)
        result = await conn.fetch(query)

    return web.Response(body=str(result))