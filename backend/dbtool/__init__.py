import sys
import asyncio
import json
import string
import random
from hashlib import md5
from prisma import Prisma


"""
expects dictionary as follows:
{
    "email": "email@server.tld"
    "password": "abc123"
}
"""

async def create_user(user):
    db = await connect()
    salt = ''.join(random.choices(string.ascii_uppercase+string.digits, k=10))
    passHash = md5(bytes((user["password"]+salt), 'utf-8')).hexdigest()
    user_obj = {"email":user["email"], "passHash":passHash,"salt":salt}
    user_in_db = await db.user.create(data=user_obj)
    resume_in_db =  await create_resume(user_in_db.id)
    await db.disconnect()
    return user_in_db, resume_in_db


"""
returns all user entries 
"""
async def get_users():
    db = await connect()
    users_in_db = await db.user.find_many()
    await db.disconnect()
    return users_in_db


"""
returns a user entry by id
expects an a str or int, see int() cast
"""

async def get_user(userId):
    db = await connect()
    user_in_db = await db.user.find_unique(
            where={
                'id':int(userId),
                }
        )
    await db.disconnect()
    return user_in_db


""" 
creates basic in db
expects dictionary object as follows:
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

async def create_basic(basics):
    db = await connect()
    await db.disconnect()
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

async def create_location(location):
    db = await connect()
    created_location = await db.location.create(location)
    await db.disconnect()
    return created_location

"""
creates an empty resume for user
expects userId as int or string, see int() cast
"""

async def create_resume(userId):
    db = await connect()
    created_resume = await db.resume.create(data={
                'belongsToId': int(userId)
            })
    
    created_resume1 = await db.resume.update(
        where={
            'belongsToId': int(userId),
        },
        data={
            'belongsTo': {
                'connect':{'id':int(userId)},
            }
        }
    )
    await db.disconnect()
    return (created_resume1)

"""
delete resume by userId
"""
async def delete_resume(userId):
    db = await connect()
    deleted_resume = await db.resume.delete(
    where={
        'belongsToId':int(userId),
    },
)
    await db.disconnect()
    return deleted_resume

"""
returns a resume entry by id
expects an a str or int, see int() cast
"""

async def get_resume(userId):
    db = await connect()
    resume_in_db = await db.resume.find_unique(
            where={
                'belongsToId':int(userId),
                }
        )
    await db.disconnect()
    return resume_in_db

"""
initializes db connection
"""

async def connect():
    db = Prisma()
    await db.connect()
    return db

"""
handles cli testing of interface during development
"""

async def main(arg0,arg1):
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
    ret =  asyncio.run(main(sys.argv[1],sys.argv[2]))
    print(ret)
