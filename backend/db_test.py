import sys
import asyncio
import json
import dbtool
import scratches

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
            logged_out = await dbtool.logout(arg1)
            return logged_out
        case "get_all_authorized":
            all_authorized = await dbtool.get_all_authorized()
            return all_authorized
        case "get_authorized_by_user_id":
            authorized = await dbtool.get_authorized_by_user_id(arg1)
            return authorized
        case "get_authorized_by_token":
            authorized = await dbtool.get_authorized_by_token(arg1)
            return authorized
        case "is_authorized":
            is_authorized_state = await dbtool.is_authorized(arg1)
            return is_authorized_state
        case "user_from_token":
            user = await dbtool.user_from_token(arg1)
            return user
        case "create_location":
            location = await dbtool.create_location(arg1,arg2)
            return location
        case "create_basics":
            basics = await dbtool.create_basics(arg1,arg2)
            return basics
        case "get_basics":
            basics = await dbtool.get_basics(arg1)
            return basics
        case "get_all_basics":
            basics = await dbtool.get_all_basics()
            return basics
        case "create_summary":
            summary = await dbtool.create_summary(arg1,arg2)
            return summary
        case "delete_basics":
            deleted_basics = await dbtool.delete_basics(arg1)
            return deleted_basics
        case "update_basics":
            new_basics = await dbtool.update_basics(arg1,arg2)
            return new_basics
        case "get_resume_json":
            resume_json = await dbtool.get_resume_json(arg1)
            return resume_json
        case "test_raw":
            test = await dbtool.get_resume_clean(arg1)
            return test
        case "query_raw":
            ret = await dbtool.query_raw("*",arg1,arg2)
            return ret
        case "snakeCaser":
            snake_case = dbtool.convert_to_snake(arg1)
            return snake_case
        case "update_resume":
            updated_resume = await dbtool.update_resume(scratches.testy_resume(),arg1)
            return updated_resume
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
