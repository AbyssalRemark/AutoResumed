import sys
import asyncio
import json
import string
import random
from hashlib import md5
from prisma import Prisma

async def create_user(db, user):
    """
    Expects dictionary as follows:
    {
        "email": "email@server.tld"
        "password": "abc123"
    }
    """
    salt = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    pass_hash = md5(bytes((user["password"] + salt), "utf-8")).hexdigest()
    user_obj = {"email": user["email"], "passHash": pass_hash, "salt": salt}
    user_in_db = await db.user.create(data=user_obj)
    resume_in_db = await create_resume(user_in_db.id)
    return user_in_db, resume_in_db


async def get_all_users(db):
    """
    Returns all user entries
    """
    users_in_db = await db.user.find_many()
    return users_in_db


async def get_user(db, user_id):
    """
    Returns a user entry by id
    Expects a str or int, see int() cast
    """
    user_in_db = await db.user.find_unique(
        where={
            "id": int(user_id),
        },
        include={
           'resume':True
        }
    )
    return user_in_db


async def create_basic(db, basics):
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
    print("todo")


async def create_location(db, location, token):
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
    created_location = await db.location.create(location)
    return created_location


async def create_resume(db, userId):
    """
    Creates an empty resume for user
    Expects userId as int or string, see int() cast
    """
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


async def delete_resume(db, userId):
    """
    Delete resume by userId
    Expects userId as int or string, see int() cast
    """
    deleted_resume = await db.resume.delete(
        where={
            "belongsToId": int(userId),
        },
    )
    return deleted_resume


async def get_resume(db, userId):
    """
    Returns a resume entry by id
    Expects a str or int, see int() cast
    """
    resume_in_db = await db.resume.find_unique(
        where={
            "belongsToId": int(userId),
        },
        include={
            "belongsTo":True
        }
    )
    return resume_in_db

async def login(db, credential):
    """
    Returns an auth token
    Expects a dictionary of form:
    {
        email:email@email.com
        password:password
    }
    """
    user = await db.user.find_unique(
        where={
            "email":credential["email"]
        }
    )
    token = None
    authorized = None
    if(check_pass_hash(user,credential["password"])):
        
        seedA = "".join(random.choices(string.ascii_uppercase + string.digits, k=100))
        tokenA = str(md5(bytes((seedA), "utf-8")).hexdigest())
        seedB = "".join(random.choices(string.ascii_uppercase + string.digits, k=100))
        tokenB = str(md5(bytes((seedB), "utf-8")).hexdigest())
        token = str(tokenA+tokenB)
        auth_obj={"belongsToId":user.id,"token":token}
        authorized = await db.authorized.create(data=auth_obj)
        authorized = await db.authorized.update(
            where={"belongsToId":authorized.belongsToId},
            data={"belongsTo":{"connect":{"id":user.id}}}
        )
    return token

async def user_from_token(db, token):
    """
    returns the user entry related to a token
    """
    auth_in_db = await db.authorized.find_unique(
        where={
            "token":token,
        },
        include={
            'belongsTo':True,
        }
    )
    return auth_in_db.belongsTo

 
async def logout(db, token):
    """
    logs you out using token
    """
    authorized = await db.authorized.find_unique(
        where={"token":token["token"]}
    )
    print(authorized)
    authorized = await db.authorized.delete(
        where={"token":token["token"]}
    )
    return authorized


def check_pass_hash(user,password):
    salt = user.salt
    pass_hash = md5(bytes((password + salt), "utf-8")).hexdigest()
    if (pass_hash == user.passHash):
        return True
    else:
        return False

async def get_all_authorized(db):
    all_authorized = await db.authorized.find_many()
    return all_authorized

async def get_authorized_by_user_id(db, user_id):
    authorized = await db.authorized.find_unique(
        where={"belongsToId":int(user_id)}
    )
    return authorized

async def get_authorized_token(db, token):
    authorized = await db.authorized.find_unique(
        where={"token":token}
    )
    return authorized

async def is_authorized(db, token):
    try:
        authorized = await get_authorized_token(db, token)
        return True
    except:
        return False

"""
async def get_autho_hardcode():
    NOW DEPRECIATED
    this test code helped determine that the token 
    must be cast as a string prior to storage in 
    the authorize function

    db = await connect()
    autho = await db.authorized.find_unique(
        where={'id':2}
    )
    print(autho)
    print(autho.token)
    authorized = await db.authorized.find_unique(
        where={"token":autho.token}
    )
    await db.disconnect()
    return authorized
"""

async def connect():
    """
    Initializes DB connection
    """
    db = Prisma()
    await db.connect()
    return db


db = asyncio.run(connect())


async def main(arg0, arg1):
    """
    CLI tool, argument handler
    Handles CLI testing of interface during development
    """
    global db
    arg2 = json.loads(arg1)
    function = arg0
    match function:
        case "create_user":
            created_user = await create_user(db, arg2)
            return created_user
        case "get_all_users":
            users = await get_all_users(db)
            return users
        case "get_user":
            user = await get_user(db,arg2)
            return user
        case "create_resume":
            created_resume = await create_resume(db,arg2)
            return created_resume
        case "delete_resume":
            deleted_resume = await delete_resume(db,arg2)
            return deleted_resume
        case "get_resume":
            resume = await get_resume(db,arg2)
            return resume
        case "login":
            token = await login(db,arg2)
            return token
        case "logout":
            confirm = await logout(db,arg2["token"])
            return confirm
        case "get_all_authorized":
            all_authorized = await get_all_authorized()
            return all_authorized
        case "get_authorized_by_user_id":
            authorized = await get_authorized_by_user_id(db,arg2)
            return authorized
        case "get_authorized_token":
            authorized = await get_authorized_token(db,arg2["token"])
            return authorized
        case "is_authorized":
            is_authorized_state = await is_authorized(db,arg2["token"])
            return is_authorized_state
        case "user_from_token":
            user = await user_from_token(db,arg1)
            return user
        case _:
            return "wrong use, try harder"


if __name__ == "__main__":
    ret = asyncio.run(main(sys.argv[1], sys.argv[2]))
    print(ret)
