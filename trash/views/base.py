# from datetime import datetime
# from aiohttp_session import get_session
# from aiohttp import web
# from sqlalchemy import select
# from aiohttp_jinja2 import template
# from trash import db
#
#
# # class Index(web.View):
# #     async def get(self):
# #         conf = self.app['config']
# #         return web.Response(text='Hello')
#
#
# @template('index.html')
# async def index(request):
#     app_name = request.app['config'].get('app_name')
#     return {'app_name': app_name}
#
#
# async def post(request):
#     async with request.app['db'].acquire() as conn:
#         query = select([db.post.c.id, db.post.c.title])  # если отдные entries [db.post.c.id, db.post.c.title]
#         print(query)
#         result = await conn.fetch(query)
#         result = list(map(lambda r: {"id": r.get("id"), "title": r.get("title")}, result))
#
#         # def lambda_simulation(r):
#         #     return {"id": r.get("id"), "title": r.get("title")}
#         #
#         # result_list_of_dict = []
#         # for record in result:
#         #     record_dict = lambda_simulation(record)
#         #     result_list_of_dict.append(record_dict)
#
#     return web.json_response(result)
#
#
# class Login(web.View):
#     async def get(self):
#         session = await get_session(self)
#         session['last_visit'] = str(datetime.utcnow())
#         last_visit = session['last_visit']
#         # if 'last_visit' in session else None
#         text = 'Last v isited: {}'.format(last_visit)
#         return web.Response(text='Login {}'.format(text))
#
#     async def post(self):
#         return web.Response(text='login')
#
#
# # async def login(request):
# #     return web.Response(text='LOGIN')
#
#
# class Signup(web.View):
#     async def get(self):
#         return web.Response(text='signup')
