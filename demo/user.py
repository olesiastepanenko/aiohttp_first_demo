# простой класс для манипуляции с бд

class User:
    collection = None
    def __init__(self):
        pass
    @staticmethod
    async def get_user(db, user_id): # ф-я принимает бд
        return await db.users.find_one(user_id) #users - это имя коллекции