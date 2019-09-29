from sqlalchemy import create_engine, MetaData

from demo.settings import config
from demo.db import posts, comments


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

def create_tables(engine):
    meta = MetaData()

    meta.create_all(bind=engine, tables=[posts, comments])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(posts.insert(), [
        {'title': 'What\'s new?',
         'message': 'Hello world, it\'s how are you?',
         'pub_date': '2019-09-29 10:17:49.629+02'}
    ])
    conn.execute(comments.insert(), [
        {'comment_text': 'Not much', 'votes': 0, 'posts_id': 1},
        {'comment_text': 'The sky', 'votes': 0, 'posts_id': 1},
        {'comment_text': 'Just hacking again', 'votes': 0, 'posts_id': 1},
    ])

    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)