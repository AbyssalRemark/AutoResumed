import sys
import asyncio
import json
import dbtool

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
            created_user = await dbtool.create_user(arg1)
            return created_user
        case "get_all_users":
            users = await dbtool.get_all_users()
            return users
        case "get_user":
            user = await dbtool.get_user(arg1)
            return user
        case "delete_user":
            deleted_user = await dbtool.delete_user(arg1)
            return deleted_user
        case "delete_user_cascade":
            deleted_user = await dbtool.delete_user_cascade(arg1)
            return deleted_user
        case "create_resume_blank":
            created_resume = await dbtool.create_resume_blank(arg1)
            return created_resume
        case "delete_resume":
            deleted_resume = await dbtool.delete_resume(arg1)
            return deleted_resume
        case "get_resume":
            resume = await dbtool.get_resume(arg1)
            return resume
        case "login":
            token = await dbtool.login(arg1)
            return token
        case "logout":
            logged_out = await dbtool.logout(arg1["token"])
            return logged_out
        case "get_all_authorized":
            all_authorized = await dbtool.get_all_authorized()
            return all_authorized
        case "get_authorized_by_user_id":
            authorized = await dbtool.get_authorized_by_user_id(arg1)
            return authorized
        case "get_authorized_by_token":
            authorized = await dbtool.get_authorized_by_token(arg1["token"])
            return authorized
        case "is_authorized":
            is_authorized_state = await dbtool.is_authorized(arg1["token"])
            return is_authorized_state
        case "user_from_token":
            user = await dbtool.user_from_token(arg1["token"])
            return user
        case "create_location":
            location = await dbtool.create_location(arg1,arg2)
            return location
        case "create_basic":
            basic = await dbtool.create_basic(arg1,arg2)
            return basic
        case "get_basic":
            basic = await dbtool.get_basic(arg1)
            return basic
        case "get_all_basic":
            basics = await dbtool.get_all_basic()
            return basics
        case "create_summary":
            summary = await dbtool.create_summary(arg1,arg2)
            return summary
        case "delete_basic":
            deleted_basic = await dbtool.delete_basic(arg1)
            return deleted_basic
        case _:
            return "wrong use, try harder"


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

