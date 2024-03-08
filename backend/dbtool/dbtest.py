import sys
import asyncio
import json
import dbtools

async def dbtest(argA, argB, argC):
    """
    CLI tool, argument handler
    Handles CLI testing of interface during development
    """
    try:
        arg1 = json.loads(argB)
    except:
        arg1 = argB
    try:
        arg2 = json.loads(argC)
    except:
        arg2 = argC

    match argA:
        case "create_user":
            created_user = await dbtools.create_user(arg1)
            return created_user
        case "get_all_users":
            users = await dbtools.get_all_users()
            return users
        case "get_user":
            user = await dbtools.get_user(arg1)
            return user
        case "delete_user":
            deleted_user = await dbtools.delete_user(arg1)
            return deleted_user
        case "create_resume_blank":
            created_resume = await dbtools.create_resume_blank(arg1)
            return created_resume
        case "delete_resume":
            deleted_resume = await dbtools.delete_resume(arg1)
            return deleted_resume
        case "get_resume":
            resume = await dbtools.get_resume(arg1)
            return resume
        case "login":
            token = await dbtools.login(arg1)
            return token
        case "logout":
            logged_out = await dbtools.logout(arg1["token"])
            return logged_out
        case "get_all_authorized":
            all_authorized = await dbtools.get_all_authorized()
            return all_authorized
        case "get_authorized_by_user_id":
            authorized = await dbtools.get_authorized_by_user_id(arg1)
            return authorized
        case "get_authorized_by_token":
            authorized = await dbtools.get_authorized_by_token(arg1["token"])
            return authorized
        case "is_authorized":
            is_authorized_state = await dbtools.is_authorized(arg1["token"])
            return is_authorized_state
        case "user_from_token":
            user = await dbtools.user_from_token(arg1["token"])
            return user
        case "create_location":
            location = await dbtools.create_location(arg1,arg2)
            return location
        case "create_basic":
            basic = await dbtools.create_basic(arg1,arg2)
            return basic
        case "get_basic":
            basic = await dbtools.get_basic(arg1)
            return basic
        case "get_all_basic":
            basics = await dbtools.get_all_basic()
            return basics
        case "create_summary":
            summary = await dbtools.create_summary(arg1,arg2)
            return summary
        case "delete_basic":
            deleted_basic = await dbtools.delete_basic(arg1)
            return deleted_basic
        case "update_basic":
            new_basic = await dbtools.update_basic(arg1,arg2)
            return new_basic
        case "get_resume_json":
            resume_json = await dbtools.get_resume_json(arg1)
            return resume_json
        case "test_raw":
            test = await dbtools.get_resume_clean(arg1)
            return test
        case "query_raw":
            ret = await dbtools.query_raw("*",arg1,arg2)
            return ret
        case _:
            return "incorrect function load"


if __name__ == "__main__":
    match len(sys.argv):
        case 2:
            ret = asyncio.run(dbtest(sys.argv[1], "", ""))
            print(ret)
        case 3:
            ret = asyncio.run(dbtest(sys.argv[1], sys.argv[2], ""))
            print(ret)
        case 4:
            ret = asyncio.run(dbtest(sys.argv[1], sys.argv[2], sys.argv[3]))
            print(ret)
        case _:
            print("oopsie, not a viable use!")