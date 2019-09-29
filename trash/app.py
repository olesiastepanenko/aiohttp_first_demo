# import base64
# from cryptography import fernet
# from aiohttp_session import setup
# from aiohttp_session.cookie_storage import EncryptedCookieStorage
# from aiohttp import web
# import jinja2
# import aiohttp_jinja2
# from trash.routes import setup_routes
# import asyncpgsa
#
#
#
# async def create_app(config:dict):
#     app = web.Application()#создаем объект приложения
#     #сессия
#     fernet_key = fernet.Fernet.generate_key() #генерируем ключ для сессии
#     secret_key = base64.urlsafe_b64decode(fernet_key)
#     setup(app, EncryptedCookieStorage(secret_key))
#     #в словаре приложения создаем новый ключ config
#     app['config'] = config
#     aiohttp_jinja2.setup(
#         app,
#         loader = jinja2.PackageLoader('demo', 'templates')
#     )#добавляем поддержку jinja2 шаблонов
#     setup_routes(app)
#     app.on_startup.append(on_start)
#     app.on_cleanup.append(on_shutdown )#при закрытии сайта закрываем все соединения
#     return app, secret_key
#
#
# async def on_start(app):#движок DB
#     config = app['config']#объект конфигурации находится внутри ключа config
#     # dsn = construct_db_url(app['config']['database'])
#     app['db'] = await asyncpgsa.create_pool(dsn=config['database_uri'])
#
#
# async def on_shutdown(app):
#     app['db'].close()
#
#
#
#
