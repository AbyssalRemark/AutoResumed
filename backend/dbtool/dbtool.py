import sys
import asyncio
import json
import string
import random
from hashlib import md5
from prisma import Prisma


"""
creates a user, generating some salt and hashing password+salt
expects json as follows:
{
    "email": "email@server.tld"
    "password": "abc123"
}
"""

async def create_user(db, user) -> str:
    input_obj = json.loads(user)
    salt = ''.join(random.choices(string.ascii_uppercase+string.digits, k=10))
    passHash = md5(bytes((input_obj["password"]+salt), 'utf-8')).hexdigest()
    user_obj = {"email":input_obj["email"], "passHash":passHash,"salt":salt}
    print(user_obj)
    user_in_db = await db.user.create(user_obj)
    return user_in_db

async def get_users(db) -> str:
    users_in_db = await db.user.find_many()
    return users_in_db


"""
expects an a str or int, see int() cast
"""

async def get_user(db, userId):
    user_in_db = await db.user.find_unique(
            where={
                'id':int(userId),
                }
        )
    return user_in_db

"""
TODO: build this up
"""

async def create_resume(db, resume, userId) -> str:
    resume_obj = json.loads(resume)
    created_resume = await db.resume.create(data=resume_obj)
    return (created_resume)


async def get_resume(db, userId) -> str:
    resume_in_db = await db.user.find_unique(
            where={
                'belongsToId':int(userId),
                }
        )
    return user_in_db

async def connect() -> None:
    db = Prisma()
    await db.connect()
    return db

async def main(arg1,arg2) -> str:
    function = arg1
    db = await connect()
    match function:
        case "create_user":
            created_user = await create_user(db, arg2)
            return created_user
        case "get_users":
            users = await get_users(db)
            return users
        case "get_user":
            user = await get_user(db,arg2)
            return user
        case "create_resume":
            created_resume = await create_resume(db, arg2,1)
            return created_resume
        case _:
            print("wrong use, try harder")
            return "wrong use, try harder"



if __name__ == "__main__":
    ret =  asyncio.run(main(sys.argv[1],sys.argv[2]))
    print(ret)