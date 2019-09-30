# import aiopg.sa
# from sqlalchemy import (
#     MetaData, Table, Column, ForeignKey,
#     Integer, String, Date
# )
#
# meta = MetaData()
#
# posts = Table(
#     'posts', meta,
#     Column('id', Integer, primary_key=True),
#     Column('title', String(200), nullable=False),
#     Column('message', String(500), nullable=False),
#     Column('pub_date', Date, nullable=False),
# )
#
# comments = Table(
#     'comments', meta,
#     Column('id', Integer, primary_key=True),
#     Column('comment_text', String(200), nullable=False),
#     Column('votes', Integer, server_default="0", nullable=False),
#     Column('post_id',
#            Integer,
#            ForeignKey('posts.id', ondelete='CASCADE'))
# )
#
#
# class RecordNotFound(Exception):
#     """Requested record in database was not found"""
#
#
# async def init_pg(app):  # engine instance for making DB queries
#     conf = app['config']['postgres']
#     engine = await aiopg.sa.create_engine(
#         database=conf['database'],
#         user=conf['user'],
#         password=conf['password'],
#         host=conf['host'],
#         port=conf['port'],
#         minsize=conf['minsize'],
#         maxsize=conf['maxsize'],
#     )
#     app['db'] = engine
#
#
# async def close_pg(app):
#     app['db'].close()
#     await app['db'].wait_closed()
#
#
# async def get_posts(conn, post_id):
#     result = await conn.execute(  # пишем запрос в бд
#         posts.select()
#         .where(posts.c.id == post_id))
#     post_record = await result.first()
#     if not post_record:  # если записей нет
#         msg = 'Post with ID: {} does not exist'
#         raise RecordNotFound(msg.format(post_id))
#     result = await conn.execute(
#         comments.select()
#         .where(comments.c.post_id == post_id)
#         .order_by(comments.c.id))
#     comment_record = await result.fetchall()
#     return post_record, comment_record
#
#
# async def vote(conn, post_id, comment_id):
#     result = await conn.execute(
#         comments.update()
#         .returning(*comments.c)
#         .where(comments.c.id == comment_id)
#         .values(votes=comments.c.votes+1))
#     record = await result.fetchone()
#     if not record:
#         msg = "Post with id: {} or comment id: {} does not exists"
#         raise RecordNotFound(msg.format(post_id, comment_id))
#
