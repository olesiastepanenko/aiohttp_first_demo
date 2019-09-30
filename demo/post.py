from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime


class Post:

    @staticmethod
    async def create_post(db: AsyncIOMotorDatabase, post_text: str, title: str):
        data = {
            # 'user_id': ObjectId(user_id),
            'title': title,
            'post_text': post_text,
            'date_created': datetime.utcnow()
        }
        await db.posts.insert_one(data)

    @staticmethod
    async def get_post(db: AsyncIOMotorDatabase, limit=20):
        posts = await db.posts.find().to_list(limit)
        return posts

    @staticmethod
    async def get_post_detail_by_id(db: AsyncIOMotorDatabase, post_id):
        current_post = await db.posts.find_one({'_id': ObjectId(post_id)})
        return current_post