import sys
import asyncio
import json
import string
import random
from hashlib import md5
from prisma import Prisma


"""
creates a user entry, generating some salt and hashing password+salt
expects json as follows:
{
    "email": "email@server.tld"
    "password": "abc123"
}
"""


async def create_user(db, user) -> str:
    input_obj = json.loads(user)
    salt = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    pass_hash = md5(bytes((input_obj["password"] + salt), "utf-8")).hexdigest()
    user_obj = {"email": input_obj["email"], "passHash": pass_hash, "salt": salt}
    user_in_db = await db.user.create(user_obj)

    return user_in_db


"""
returns all user entries 
"""


async def get_users(db):
    users_in_db = await db.user.find_many()

    return users_in_db


"""
returns a user entry by id
expects an a str or int, see int() cast
"""


async def get_user(db, userId):
    user_in_db = await db.user.find_unique(
        where={
            "id": int(userId),
        }
    )

    return user_in_db


""" 
creates basic in db
expects JSON object as follows:
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


async def create_basic(db, basics):
    print("todo")


"""
helper for create_basic, creates a location in db
expects python dictionary object as follows:
{
    "address": "2712 Broadway St",
    "postalCode": "CA 94115",
    "city": "San Francisco",
    "countryCode": "US",
    "region": "California"
}
"""


async def create_location(db, location):
    created_location = await db.location.create(location)

    return created_location


"""
creates an empty resume for user
expects userId as int or string, see int() cast
"""


async def create_resume(db, userId):
    created_resume = await db.resume.create(data={"belongsToId": int(userId)})

    created_resume = await db.resume.update(
        where={
            "belongsToId": int(userId),
        },
        data={
            "belongsTo": {
                "connect": {"id": int(userId)},
            }
        },
    )

    return created_resume


"""
delete resume by userId
"""


async def delete_resume(db, userId):
    deleted_resume = await db.resume.delete(
        where={
            "belongsToId": int(userId),
        },
    )

    return deleted_resume


"""
returns a resume entry by id
expects an a str or int, see int() cast
"""


async def get_resume(db, userId):
    resume_in_db = await db.user.find_unique(
        where={
            "belongsToId": int(userId),
        }
    )

    return resume_in_db


"""
Initializes db connection
"""


async def connect():
    db = Prisma()
    await db.connect()

    return db


"""
Handles cli testing of interface during development
"""


async def main(arg1, arg2):
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
            user = await get_user(db, arg2)
            return user
        case "create_resume":
            created_resume = await create_resume(db, arg2)
            return created_resume
        case "delete_resume":
            deleted_resume = await delete_resume(db, arg2)
            return deleted_resume

        case _:
            print("wrong use, try harder")
            return "wrong use, try harder"


if __name__ == "__main__":
    ret = asyncio.run(main(sys.argv[1], sys.argv[2]))
    print(ret)
