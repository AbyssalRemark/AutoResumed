import sys
import asyncio
import json
import string
import random
from hashlib import md5
from prisma import Prisma


async def create_user(user: dict[str, str]):
    """
    Expects dictionary as follows:
    {
        "email": "email@server.tld"
        "password": "abc123"
    }
    """
    db = await connect()
    salt = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    passHash = md5(bytes((user["password"] + salt), "utf-8")).hexdigest()
    user_obj = {"email": user["email"], "passHash": passHash, "salt": salt}
    user_in_db = await db.user.create(data=user_obj)
    resume_in_db = await create_resume(user_in_db.id)
    await db.disconnect()
    return user_in_db, resume_in_db


async def get_users():
    """
    Returns all user entries
    """
    db = await connect()
    users_in_db = await db.user.find_many()
    await db.disconnect()
    return users_in_db


async def get_user(userId: str | int):
    """
    Returns a user entry by id
    Expects a str or int, see int() cast
    """
    db = await connect()
    user_in_db = await db.user.find_unique(
        where={
            "id": int(userId),
        }
    )
    await db.disconnect()
    return user_in_db


async def create_basic(basics):
    """
    Creates basic in db
    Expects dictionary object as follows:
    {
    "basics": {
            "name": "John Doe",
            "label": [{
            "tags":["tag"],
            "label":"Programmer"
            }],
            "image": "https://somesite.tld/img.png",
            "email": "john@gmail.com",
            "phone": "(912) 555-4321",
            "url": "https://johndoe.com",
            "summary": [{
            "tags":["tag"],
            "summary":"A summary of John Doe…"
            }],
            "location": {
            "address": "2712 Broadway St",
            "postalCode": "CA 94115",
            "city": "San Francisco",
            "countryCode": "US",
            "region": "California"
            },
            "profiles": [{
            "tags": ["tag"],
            "network": "Twitter",
            "username": "john",
            "url": "https://twitter.com/john"
            }]
        },
    "userId":"123",
    "token":"abc123"
    }
    """
    db = await connect()
    await db.disconnect()
    print("todo")


async def create_location(location):
    """
    Helper for create_basic, creates a location in db
    Expects python dictionary object as follows:
    {
        "address": "2712 Broadway St",
        "postalCode": "CA 94115",
        "city": "San Francisco",
        "countryCode": "US",
        "region": "California"
    }
    """
    db = await connect()
    created_location = await db.location.create(location)
    await db.disconnect()
    return created_location


async def create_resume(userId: str | int):
    """
    Creates an empty resume for user
    Expects userId as int or string, see int() cast
    """
    db = await connect()
    created_resume = await db.resume.create(data={"belongsToId": int(userId)})

    created_resume1 = await db.resume.update(
        where={
            "belongsToId": int(userId),
        },
        data={
            "belongsTo": {
                "connect": {"id": int(userId)},
            }
        },
    )
    await db.disconnect()
    return created_resume1


async def delete_resume(userId: str | int):
    """
    Delete resume by userId
    Expects userId as int or string, see int() cast
    """
    db = await connect()
    deleted_resume = await db.resume.delete(
        where={
            "belongsToId": int(userId),
        },
    )
    await db.disconnect()
    return deleted_resume


async def get_resume(userId: str | int):
    """
    Returns a resume entry by id
    Expects a str or int, see int() cast
    """
    db = await connect()
    resume_in_db = await db.resume.find_unique(
        where={
            "belongsToId": int(userId),
        }
    )
    await db.disconnect()
    return resume_in_db


async def connect():
    """
    Initializes DB connection
    """
    db = Prisma()
    await db.connect()
    return db


async def main(arg0, arg1):
    """
    Handles CLI testing of interface during development
    """
    function = arg0
    arg2 = json.loads(arg1)
    match function:
        case "create_user":
            created_user = await create_user(arg2)
            return created_user
        case "get_users":
            users = await get_users()
            return users
        case "get_user":
            user = await get_user(arg2)
            return user
        case "create_resume":
            created_resume = await create_resume(arg2)
            return created_resume
        case "delete_resume":
            deleted_resume = await delete_resume(arg2)
            return deleted_resume

        case "get_resume":
            resume = await get_resume(arg2)
            return resume
        case _:
            return "wrong use, try harder"


if __name__ == "__main__":
    ret = asyncio.run(main(sys.argv[1], sys.argv[2]))
    print(ret)
