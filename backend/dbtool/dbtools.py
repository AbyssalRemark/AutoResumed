import string
import random
import camel_caser
import snakeCaser
#from camel_caser import convert_to_camel
#from snakeCaser import convert_to_snake
import json
import asyncio
from hashlib import sha256
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
        pass_hash = sha256(bytes((user["password"] + salt), "utf-8")).hexdigest()
        user_obj = {"email": user["email"], "pass_hash": pass_hash, "salt": salt}
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


async def delete_user(token, db=None):
    """
    Deletes user account and all associated data from our database
    """
    if db==None:
        async with Prisma() as db:
            deleted_user = await delete_user(token,db)
    else:
        auth = await get_authorized_by_token(token)
        user_id = auth.belongs_to_id
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
    originally thought we'd have to delete each foreign table entry individually
    best practice is to use the onDelete:Cascade relation feature
 
    async with Prisma() as db:
        authorized_user = await db.authorized.find_unique(
            where={
                "token":token
            },
            include={
                "belongs_to":True
            }
        )
        user_id = authorized_user.belongs_to.id
        print(authorized_user.belongs_to.id)
        await db.resume.delete(
            where={
                "belongs_to_id":user_id
            }
        )
        await db.authorized.delete(
            where={
                "belongs_to_id":user_id
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
        created_resume = await db.resume.create(data={"belongs_to_id": int(user_id)})
        """
        Turns out the relational connection is automatic!!
        had to figure that out the beat-your-head-against-the-wall way
        created_resume = await db.resume.update(
            where={
                "belongs_to_id": int(user_id),
            },
            data={
                "belongs_to": {
                    "connect": {"id": int(user_id)},
                }
            },
        )
        """
    return created_resume


async def delete_resume(token, db=None):
    """
    Delete resume by userId
    Expects userId as int or string, see int() cast
    """
    if db == None:
        async with Prisma() as db:
            deleted_resume = await delete_resume(token,db)
    
    else:
        user = await user_from_token(token)
        deleted_resume = await db.resume.delete(
            where={
                "belongs_to_id": user.id,
            },
        )
    return deleted_resume

async def update_resume(resume, token, db=None):
    """
    Updates resume, since this is a very bulky object, we have elected to delete
    and create anew, as it is likely more efficient then checking for difference
    """
    if db == None:
        async with Prisma() as db:
            updated_resume = await update_resume(resume, token,db)

    else:
        user_id = (await delete_resume(token,db)).belongs_to_id
        resume_id = (await create_resume_blank(user_id, db)).id
        resume = snakeCaser.convert_to_snake(resume)

        try:
            await create_basic(resume["basic"], token, resume_id, db)
        except:
            pass

        try:
            await create_work(resume["work"], resume_id, db)
        except:
            pass

        try:
            await create_volunteer(resume["volunteer"], resume_id, db)
        except:
            pass

        try:
            await create_education(resume["education"], resume_id, db)
        except:
            pass

        try:
            await create_award(resume["award"], resume_id, db)
        except:
            pass

        try:
            await create_certificate(resume["certificate"], resume_id, db)
        except:
            pass

        try:
            await create_publication(resume["publication"], resume_id, db)
        except:
            pass

        try:
            await create_skill(resume["skill"], resume_id, db)
        except:
            pass

        try:
            await create_language(resume["language"], resume_id, db)
        except:
            pass

        try:
            await create_interest(resume["interest"], resume_id, db)
        except:
            pass

        try:
            await create_reference(resume["reference"], resume_id, db)
        except:
            pass

        try:
            await create_project(resume["project"], resume_id, db)
        except:
            pass

        try:
            if resume["tags"] != []:
                await db.resume.update(
                    where={"id":resume_id},
                    data={"tags":resume["tags"]}
                )
        except:
            pass


        updated_resume = await db.resume.find_unique(
            where={
               "id": resume_id,
            },
            include={
                "belongs_to":True,
                "basic":True,
                "work":True,
                "volunteer":True,
                "education":True,
                "award":True,
                "certificate":True,
                "publication":True,
                "skill":True,
                "language":True,
                "interest":True,
                "reference":True,
                "project":True,
                "tags":True
            }
        )
    return updated_resume


async def get_resume(token,db=None):
    """
    Returns a resume entry by token, cli/admin function, not for getting valid json object contents
    """
    if db == None:
        async with Prisma() as db:
            resume_in_db = await get_resume(token,db)
    else:
        user = await user_from_token(token,db)
        #Note the include= keyword in the find_unique call, critical stuff
        resume_in_db = await db.resume.find_unique(
            where={
               "belongs_to_id": user.belongs_to_id,
            },
            include={
                "belongs_to":True,
                "basic":True,
                "work":True,
                "volunteer":True,
                "education":True,
                "award":True,
                "certificate":True,
                "publication":True,
                "skill":True,
                "language":True,
                "interest":True,
                "reference":True,
                "project":True,
                "tags":True
            }
        )
    return resume_in_db

async def query_raw (fields,table,id_value,db=None):
    if db == None:
        async with Prisma() as db:
            query_out = await query_raw(fields,table,id_value,db)
    else:
        query_out = await db.query_raw(f'SELECT {fields} FROM "{table}" WHERE "{table}".belongs_to_id = {id_value}')
    return query_out

async def get_resume_clean(token, db=None):
    if db==None:
        async with Prisma() as db:
            clean_resume = await get_resume_clean(token,db)
    else:
        auth = await get_authorized_by_token(token,db)
        resume = await db.resume.find_unique(
            where={"belongs_to_id":auth.belongs_to_id}
        )
        basic = await query_raw("id,name,image,email,phone,url","Basic",resume.id,db)
        basic_id = basic[0].pop("id")
        basic = basic[0]
        summary = await query_raw("tags,summary","Summary",resume.id,db)
        label = await query_raw("tags,label","Label",resume.id,db)
        location = await query_raw("address,postal_code,city,country_code,region","Location",basic_id,db)
        location = location[0]
        profiles = await query_raw("tags,network,username,url","Profile",resume.id,db)
        basic["summary"] = summary
        basic["label"] = label
        basic["location"] = location
        basic["profiles"] = profiles
        work = await query_raw("tags,name,position,url,start_date,end_date,summary,highlights","Work",resume.id,db)
        volunteer = await query_raw("tags,organization,position,url,start_date,end_date,summary,highlights","Volunteer",resume.id,db)
        education = await query_raw("tags,institution,url,area,study_type,start_date,end_date,score,courses","Education",resume.id,db)
        award = await query_raw("tags,title,date,awader,summary","Award",resume.id,db)
        certificate = await query_raw("tags,name,date,issuer,url","Certificate",resume.id,db)
        publication = await query_raw("tags,name,publisher,release_date,url,summary","Publication",resume.id,db)
        skill = await query_raw("tags,name,level,keywords","Skill",resume.id,db)
        language = await query_raw("tags,language,fluency","Language",resume.id,db)
        interest = await query_raw("tags,name,keywords","Interest",resume.id,db)
        reference = await query_raw("tags,name,reference","Reference",resume.id,db)
        project = await query_raw("tags,name,start_date,end_date,description,highlights,url","Project",resume.id,db)

        snake_resume = {
            "basic": basic,
            "work": work,
            "volunteer": volunteer,
            "education": education,
            "award": award,
            "certificate": certificate,
            "publication": publication,
            "skill": skill,
            "language": language,
            "interest": interest,
            "reference": reference,
            "project": project
        }
        clean_resume = camel_caser.convert_to_camel(snake_resume)


    return clean_resume

async def create_basic(basic, token, resume_id=None, db=None):
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
            basic_in_db,location_in_db,summary_in_db,label_in_db,profiles_in_db = await create_basic(basic,token,db)

    else:
        basic = snakeCaser.convert_to_snake(basic)
        if resume_id == None:
            resume_id = (await get_resume(token, db)).id
        basic_obj = {
            "belongs_to_id": resume_id,
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
        print(basic)
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

        #create the profiles
        profiles_obj = basic["profiles"]
        profiles_in_db = []
        for profile_entry in profiles_obj:
            created_profile = await create_profile(profile_entry, basic_id, db)
            profiles_in_db.append(created_profile)

    return basic_in_db,location_in_db,summary_in_db,label_in_db,profiles_in_db

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
                "belongs_to_id":resume.id
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
        resume_dict = resume.model_dump(mode='python')
        resume_dict = camel_caser.convert_to_camel(resume_dict)
        resume_json = json.dumps(resume_dict)

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
        location["belongs_to_id"] = basic_id
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
        summary["belongs_to_id"]=basic_id
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
        label["belongs_to_id"]=basic_id
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
        profile["belongs_to_id"]=basic_id
        profile_in_db = await db.profile.create(profile)
    return profile_in_db

async def create_work(work, resume_id, db=None):
    """
    Helper for update resume, creates work entries
    """
    if db==None:
        async with Prisma() as db:
            work_in_db = await create_work(work, resume_id,db)
    else:
        work["belongs_to_id"]=resume_id
        work_in_db = await db.work.create(work)
    return work_in_db

async def create_volunteer(volunteer, resume_id, db=None):
    """
    Helper for update resume, creates volunteer entries
    """
    if db==None:
        async with Prisma() as db:
            volunteer_in_db = await create_volunteer(volunteer, resume_id,db)
    else:
        volunteer["belongs_to_id"]=resume_id
        volunteer_in_db = await db.volunteer.create(volunteer)
    return volunteer_in_db

async def create_education(education, resume_id, db=None):
    """
    Helper for update resume, creates education entries
    """
    if db==None:
        async with Prisma() as db:
            education_in_db = await create_education(education, resume_id,db)
    else:
        education["belongs_to_id"]=resume_id
        education_in_db = await db.education.create(education)
    return education_in_db

async def create_award(award, resume_id, db=None):
    """
    Helper for update resume, creates award entries
    """
    if db==None:
        async with Prisma() as db:
            award_in_db = await create_award(award, resume_id,db)
    else:
        award["belongs_to_id"]=resume_id
        award_in_db = await db.award.create(award)
    return award_in_db

async def create_certificate(certificate, resume_id, db=None):
    """
    Helper for update resume, creates certificate entries
    """
    if db==None:
        async with Prisma() as db:
            certificate_in_db = await create_certificate(certificate, resume_id,db)
    else:
        certificate["belongs_to_id"]=resume_id
        certificate_in_db = await db.certificate.create(certificate)
    return certificate_in_db

async def create_publication(publication, resume_id, db=None):
    """
    Helper for update resume, creates publication entries
    """
    if db==None:
        async with Prisma() as db:
            publication_in_db = await create_publication(publication, resume_id,db)
    else:
        publication["belongs_to_id"]=resume_id
        publication_in_db = await db.publication.create(publication)
    return publication_in_db

async def create_skill(skill, resume_id, db=None):
    """
    Helper for update resume, creates skill entries
    """
    if db==None:
        async with Prisma() as db:
            skill_in_db = await create_skill(skill, resume_id,db)
    else:
        skill["belongs_to_id"]=resume_id
        skill_in_db = await db.skill.create(skill)
    return skill_in_db

async def create_language(language, resume_id, db=None):
    """
    Helper for update resume, creates language entries
    """
    if db==None:
        async with Prisma() as db:
            language_in_db = await create_language(language, resume_id,db)
    else:
        language["belongs_to_id"]=resume_id
        language_in_db = await db.language.create(language)
    return language_in_db


async def create_interest(interest, resume_id, db=None):
    """
    Helper for update resume, creates interest entries
    """
    if db==None:
        async with Prisma() as db:
            interest_in_db = await create_interest(interest, resume_id,db)
    else:
        interest["belongs_to_id"]=resume_id
        interest_in_db = await db.interest.create(interest)
    return interest_in_db

async def create_reference(reference, resume_id, db=None):
    """
    Helper for update resume, creates reference entries
    """
    if db==None:
        async with Prisma() as db:
            reference_in_db = await create_reference(reference, resume_id,db)
    else:
        reference["belongs_to_id"]=resume_id
        reference_in_db = await db.reference.create(reference)
    return reference_in_db

async def create_project(project, resume_id, db=None):
    """
    Helper for update resume, creates project entries
    """
    if db==None:
        async with Prisma() as db:
            project_in_db = await create_project(project, resume_id,db)
    else:
        project["belongs_to_id"]=resume_id
        project_in_db = await db.project.create(project)
    return project_in_db

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



async def login(credential,db=None):
    """
    Returns an auth token
    Expects a dictionary of form:
    {
        email:email@email.com
        password:password
    }
    """
    if db==None:
        async with Prisma() as db:
            token = await login(credential,db)

    else:
        user = await db.user.find_unique(
            where={
                "email":credential["email"]
            }
        )
        token = None
        authorized = None
        if(check_pass_hash(user,credential["password"])):
            token = make_token()
            auth_obj={"belongs_to_id":user.id,"token":token}
            authorized = await db.authorized.create(data=auth_obj)
            authorized = await db.authorized.update(
                where={"belongs_to_id":authorized.belongs_to_id},
                data={"belongs_to":{"connect":{"id":user.id}}}
            )
    return token

def make_token():
    seed = "".join(random.choices(string.ascii_uppercase + string.digits, k=200))
    token = str(sha256(bytes((seed), "utf-8")).hexdigest())
    token = str(token)
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
                'belongs_to':True,
            }
        )
    print(auth_in_db)
    print("WTFFF")
    return auth_in_db

 
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
    pass_hash = sha256(bytes((password + salt), "utf-8")).hexdigest()
    if (pass_hash == user.pass_hash):
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
            where={"belongs_to_id":user_id}
        )
        return authorized

async def get_authorized_by_token(token, db=None):
    """
    expects a token string, returns the authorized entry for that token, includes user
    """
    if db==None:
        async with Prisma() as db:
            authorized = get_authorized_by_token(token,db)
    else:
        #query for authorized by token
        authorized = await db.authorized.find_unique(
            where={"token":token},
            include={'belongs_to':True}
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


if __name__ == "__main__":
    rand = random.randint(0,1000)
    created = asyncio.run(create_user({"email":f"email@server{rand}.tld","password":"password"}))
    created_token = asyncio.run(login({"email":f"email@server{rand}.tld","password":"password"}))
    print(created)
    print(created_token)