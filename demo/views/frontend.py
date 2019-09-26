import json

import asyncpg
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
        query = select([db.post.c.id, db.post.c.title])#если отдные entries [db.post.c.id, db.post.c.title]
        print(query)
        result = await conn.fetch(query)
        result = list(map(lambda r: {"id": r.get("id"), "title": r.get("title")}, result))

    return web.json_response(result)