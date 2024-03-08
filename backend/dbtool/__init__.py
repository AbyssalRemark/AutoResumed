import json
from re import DOTALL
import string
import random
from hashlib import md5
from prisma import Prisma

async def create_user(user):
    """
    Expects dictionary as follows:
    {
        "email": "email@server.tld"
        "password": "abc123"
    }
    """
    async with Prisma() as db:
        salt = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        pass_hash = md5(bytes((user["password"] + salt), "utf-8")).hexdigest()
        user_obj = {"email": user["email"], "passHash": pass_hash, "salt": salt}
        user_in_db = await db.user.create(data=user_obj)
        resume_in_db = await create_resume_blank(user_in_db.id,db)
        return user_in_db, resume_in_db


async def get_all_users():
    """
    Returns all user entries
    """
    async with Prisma() as db:
        users_in_db = await db.user.find_many()
        return users_in_db


async def get_user(user_id):
    """
    Returns a user entry by id
    Expects a str or int, see int() cast
    """
    async with Prisma() as db:
        user_in_db = await db.user.find_unique(
            where={
                "id": int(user_id),
            },
            include={
                'resume':True
            }
        )
        return user_in_db


async def delete_user_cascade(token, db=None):
    """
    Deletes user account and all associated data from our database
    """
    if db==None:
        async with Prisma() as db:
            deleted_user = await delete_user_cascade(token,db)
    else:
        auth = await get_authorized_by_token(token)
        user_id = auth.belongsToId
        deleted_user = await db.user.delete(
            where={
                "id":user_id
            }
        )
    return deleted_user


"""
async def delete_user(token):
    DEPRECIATED  ->> Left for ppham's amusement
    deletes a user by token
    best practice is to use delete_user_cascade function
    async with Prisma() as db:
        authorized_user = await db.authorized.find_unique(
            where={
                "token":token
            },
            include={
                "belongsTo":True
            }
        )
        user_id = authorized_user.belongsTo.id
        print(authorized_user.belongsTo.id)
        await db.resume.delete(
            where={
                "belongsToId":user_id
            }
        )
        await db.authorized.delete(
            where={
                "belongsToId":user_id
            }
        )
        deleted_user = await db.user.delete(
            where={
                "id":user_id
            }
        )
        return deleted_user
"""


async def create_resume_blank(user_id,db=None):
    """
    Creates an empty resume upon user creation
    Expects userId as int or string, see int() cast
    Cannot use token because user is not logged in automatically
    """
    if db==None:
        async with Prisma() as db:
            created_resume = await create_resume_blank(user_id, db)
    else:
        created_resume = await db.resume.create(data={"belongsToId": int(user_id)})
        """
        Turns out the relational connection is automatic!!
        had to figure that out the beat-your-head-against-the-wall way
        created_resume = await db.resume.update(
            where={
                "belongsToId": int(user_id),
            },
            data={
                "belongsTo": {
                    "connect": {"id": int(user_id)},
                }
            },
        )
        """
    return created_resume


async def delete_resume(token):
    """
    Delete resume by userId
    Expects userId as int or string, see int() cast
    """
    async with Prisma() as db:
        user = await user_from_token(token)
        deleted_resume = await db.resume.delete(
            where={
                "belongsToId": user.id,
            },
        )
        return deleted_resume


async def get_resume(token,db=None):
    """
    Returns a resume entry by token, cli/admin function
    """
    if db == None:
        async with Prisma() as db:
            resume_in_db = await get_resume(token,db)
    else:
        user = await user_from_token(token,db)

        #Note the include= keyword in the find_unique call, critical stuff
        resume_in_db = await db.resume.find_unique(
            where={
                "belongsToId": user.id,
            },
            include={
                "basic":True,
                "work":True,
                "volunteer":True
            }
        )
    return resume_in_db

async def create_basic(basic, token, db=None):
    """
    Creates basic in db
    Expects dictionary object as follows:
    basic = {
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
            }
    """

    if db == None:
        async with Prisma() as db:
            basic_in_db,location_in_db,summary_in_db,label_in_db,profile_in_db = await create_basic(basic,token,db)

    else:
        resume = await get_resume(token, db)
        basic_obj = {
            "belongsToId": resume.id,
            "name":basic["name"],
            "image":basic["image"],
            "email":basic["email"],
            "phone":basic["phone"],
            "url":basic["url"],
        }
        #create the basic
        basic_in_db = await db.basic.create(data=basic_obj)
        basic_id = basic_in_db.id

        #create the location
        loc_obj = basic["location"]
        location_in_db = await create_location(loc_obj, basic_id, db)

        #create the summary or summaries
        summary_obj = basic["summary"]
        summary_in_db = []
        for summary_entry in summary_obj:
            created_summary = await create_summary(summary_entry, basic_id, db)
            summary_in_db.append(created_summary)
        
        #create the label or labels
        label_obj = basic["label"]
        label_in_db = []
        for label_entry in label_obj:
            created_label = await create_label(label_entry, basic_id, db)
            label_in_db.append(created_label)

        #create the profile or profiles
        profile_obj = basic["profiles"]
        profile_in_db = []
        for profile_entry in profile_obj:
            created_profile = await create_profile(profile_entry, basic_id, db)
            profile_in_db.append(created_profile)

    return basic_in_db,location_in_db,summary_in_db,label_in_db,profile_in_db

async def get_basic(token, db=None):
    """
    gets a basic table entry from a token
    """
    if db == None:
        async with Prisma() as db:
            basic = await get_basic(token,db)
    else:
        resume = await get_resume(token, db)
        basic = await db.basic.find_unique(
            where={
                "belongsToId":resume.id
            },
            include={
                "label":True,
                "summary":True,
                "location":True,
                "profiles":True
            }
        )
    return basic    

async def get_resume_json(token,db=None):
    if db==None:
        async with Prisma() as db:
            resume_json = await get_resume_json(token,db)
    else:
        resume = await get_resume(token,db)
        resume_json = resume.model_dump(mode='python')
    return resume_json


async def get_all_basic():
    """
    utility function for cli/admin
    """
    db = await connect()
    basics = await db.basic.find_many()
    return basics

async def delete_basic(token, db=None):
    """
    utility function for cli/admin
    """
    if db==None:
        async with Prisma() as db:
            deleted_basic = await delete_basic(token,db)
    else:
        basic = await get_basic(token,db)
        deleted_basic = await db.basic.delete(
            where={
                "id":basic.id
            }
        )
    return deleted_basic


async def create_location(location, basic_id, db=None):
    """
    Helper for create_basic, creates a location
    """
    if db == None:
        async with Prisma() as db:
            created_location = await create_location(location, basic_id, db)
    else:
        location["belongsToId"] = basic_id
        created_location = await db.location.create(location)
    return created_location

async def create_summary(summary, basic_id, db=None):
    """
    Helper for create basic creates a summary
    """
    if db==None:
        async with Prisma() as db:
            summary_in_db = await create_summary(summary,basic_id,db)
    else:
        summary["belongsToId"]=basic_id
        summary_in_db = await db.summary.create(summary)
    return summary_in_db

async def create_label(label, basic_id, db=None):
    """
    Helper for create basic, creates a label
    """
    if db==None:
        async with Prisma() as db:
            label_in_db = await create_label(label,basic_id,db)
    else:
        label["belongsToId"]=basic_id
        label_in_db = await db.label.create(label)
    return label_in_db

async def create_profile(profile, basic_id, db=None):
    """
    Helper for create basic, creates profile(s)
    """
    if db==None:
        async with Prisma() as db:
            profile_in_db = await create_profile(profile,basic_id,db)
    else:
        profile["belongsToId"]=basic_id
        profile_in_db = await db.profile.create(profile)
    return profile_in_db


async def update_basic(new_basic, token, db=None):
    """
    updates a basic, requiring a new basic complient as in create_basic
    deleting and making anew is honestly cheaper than comparing bit by bit
    """
    if db==None:
        async with Prisma() as db:
            new_basic_in_db = await update_basic(new_basic,token,db)
    else:
        await delete_basic(token, db)
        new_basic_in_db = await create_basic(new_basic, token, db)
    return new_basic_in_db



async def login(credential):
    """
    Returns an auth token
    Expects a dictionary of form:
    {
        email:email@email.com
        password:password
    }
    """
    async with Prisma() as db:
        user = await db.user.find_unique(
            where={
                "email":credential["email"]
            }
        )
        token = None
        authorized = None
        if(check_pass_hash(user,credential["password"])):
            token = make_token()
            auth_obj={"belongsToId":user.id,"token":token}
            authorized = await db.authorized.create(data=auth_obj)
            authorized = await db.authorized.update(
                where={"belongsToId":authorized.belongsToId},
                data={"belongsTo":{"connect":{"id":user.id}}}
            )
        return token

def make_token():
    seedA = "".join(random.choices(string.ascii_uppercase + string.digits, k=100))
    tokenA = str(md5(bytes((seedA), "utf-8")).hexdigest())
    seedB = "".join(random.choices(string.ascii_uppercase + string.digits, k=100))
    tokenB = str(md5(bytes((seedB), "utf-8")).hexdigest())
    token = str(tokenA+tokenB)
    return token

async def user_from_token(token,db=None):
    """
    returns the user entry related to a token
    """
    if db == None:
        async with Prisma() as db:
            auth_in_db = await user_from_token(token,db)
    else:
        auth_in_db = await db.authorized.find_unique(
            where={
                "token":token,
            },
            include={
                'belongsTo':True,
            }
        )
    return auth_in_db.belongsTo

 
async def logout(token):
    """
    logs you out using token
    """
    async with Prisma() as db:
        authorized = await db.authorized.delete(
            where={"token":token}
        )
        return authorized


def check_pass_hash(user,password):
    salt = user.salt
    pass_hash = md5(bytes((password + salt), "utf-8")).hexdigest()
    if (pass_hash == user.passHash):
        return True
    else:
        return False

async def get_all_authorized():
    """
    returns all currently authorized users, primarily for testing/admins
    """
    async with Prisma() as db:
        all_authorized = await db.authorized.find_many()
        return all_authorized

async def get_authorized_by_user_id(user_id):
    """
    expects integer user id returns an authorized entry, for testing/admins
    """
    async with Prisma() as db:
        authorized = await db.authorized.find_unique(
            where={"belongsToId":int(user_id)}
        )
        return authorized

async def get_authorized_by_token(token):
    """
    expects a token string, returns the authorized entry for that token, includes user
    """
    async with Prisma() as db:
        #query for authorized by token
        authorized = await db.authorized.find_unique(
            where={"token":token},
            include={'belongsTo':True}
        )
        #update the token to same value to change lastAccessed
        await db.authorized.update(
            where={"token":token},
            data={"token":token}
        )
        return authorized

async def is_authorized(token):
    """
    Confirms a user is authorized by token, returns bool
    wrapped in try catch in case token isn't there, still returns false
    """
    try:
        authorized = await get_authorized_by_token(token)
        if authorized ==  None:
            return False
        return True
    except:
        return False

async def refresh_token(token):
    """"
    issues new token to user, expects their token and returns new token
    """
    new_token = make_token()
    async with Prisma() as db:
        authorized = await db.authorized.update(
            where={
                "token":token
            },
            data={
                "token":new_token
            }
        )
    return authorized.token

async def connect():
    db = Prisma()
    await db.connect()
    return db

