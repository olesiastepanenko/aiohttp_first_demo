# простой класс для манипуляции с бд
import hashlib
from motor.motor_asyncio import AsyncIOMotorDatabase

class User:
    collection = None
    def __init__(self):
        pass
    @staticmethod
    async def get_user(db, user_id): # ф-я принимает бд
        pass
        # return await db.users.find_one(user_id) #users - это имя коллекции

    @staticmethod
    async def create_new_user(db: AsyncIOMotorDatabase, data):
        email = data['email']
        user = await db.users.find_one({'email':email})
        if user:
            return dict(error='User with Email {} is exist'.format(email))
        if data['first_name'] and data['last_name'] and data['password']:
            data = dict(data)
            data['password'] = hashlib.sha256(data['password'].encode('utf8')).hexdigest()
            result = await db.users.insert_one(data)
            return result
        else:
            return dict(error='Missing user parameters')
