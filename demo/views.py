import asyncio
from aiohttp_session import get_session
from datetime import datetime
from aiohttp import web
import aiohttp_jinja2
from .user import User
from .post import Post


class Login(web.View):
    @aiohttp_jinja2.template('login.html')
    async def get(self):
        session = await get_session(self)
        session['last_visit'] = str(datetime.utcnow())
        last_visit = session['last_visit']
        print('last_visit', last_visit)
        db = self.app['db']
        user = await User.get_user(db, user_id=1)
        document = await db.test.find_one()
        return dict(last_visit='login Aiohttp, last visited: {}'.format(last_visit))

    async def post(self):
        pass


class Signup(web.View):
    @aiohttp_jinja2.template('signup.html')
    async def get(self):
        return dict

    async def post(self):
        data = await self.post()
        result = User.create_new_user(db=self.app['db'], data=data)
        if not result or result.get('error'):
            location = self.app.router['signup'].url_for()
            return web.HTTPFound(location=location)
        location = self.app.router['login'].url_for()
        return web.HTTPFound(location=location)


class PostView(web.View):

    async def post(self):
        data = await self.post()
        # session = await get_session(self)
        # if 'user' in session and data['message']:
        await Post.create_post(db=self.app['db'], post_text=data['post_text'], title=data['title'])
        return web.HTTPFound(location=self.app.router['index'].url_for())
        # return web.HTTPForbidden()


class Index(web.View):
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        conf = self.app['config']
        posts = await Post.get_post(db=self.app['db'])
        return dict(conf=conf, posts=posts)


@aiohttp_jinja2.template('detail.html')
async def post_detail(request):
    current_post = await Post.get_post_detail_by_id(db=request.app['db'],
                                                    post_id=request.match_info['post_id'])
    return {'current_post': current_post}

