from demo.main import app
from aiohttp import web



# async def create_app():
#     app = web.Application()
#     setup_routes(app)
#     return web.Response

# if __name__ == '__main__':
web.run_app(app)

