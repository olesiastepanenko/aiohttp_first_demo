from aiohttp import web
import aiohttp_jinja2
import jinja2
from .routes import setup_routes
from .middlewares import setup_middleware
from .settings import config, BASE_DIR #импортируем настройки конфига
# from .db import init_pg, close_pg
from motor.motor_asyncio import AsyncIOMotorClient


app = web.Application()
setup_routes(app)
setup_middleware(app)
app['config'] = config
app['db'] = AsyncIOMotorClient().lusi_mongo
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR/ 'demo' / 'templates')))#путь для лоадера фронтэнда
# app.on_startup.append(init_pg)#place for connecting to the DB
# app.on_cleanup.append(close_pg)#close the DB connection
# web.run_app(app)

