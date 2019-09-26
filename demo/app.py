from aiohttp import web
import jinja2
import aiohttp_jinja2
from .routes import setup_routes
import asyncpgsa


async def create_app(config:dict):
    app = web.Application()#создаем объект приложения
    #в словаре приложения создаем новый ключ config
    app['config'] = config
    aiohttp_jinja2.setup(
        app,
        loader = jinja2.PackageLoader('demo', 'templates')
    )#добавляем поддержку jinja2 шаблонов
    setup_routes(app)
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown )#при закрытии сайта закрываем все соединения
    return app


async def on_start(app):
    config = app['config']#объект конфигурации находится внутри ключа config
    # dsn = construct_db_url(app['config']['database'])
    app['db'] = await asyncpgsa.create_pool(dsn=config['database_uri'])


async def on_shutdown(app):
    app['db'].close()
    await app['db'].wait_closed()




