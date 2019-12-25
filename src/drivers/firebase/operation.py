from app import db
import pprint
import asyncio


async def read_from_db(key):
    try:
        data = db.child("evaluations").child(key).get()
    except Exception as error:
        print("error read: ", error)
    else:
        print("success read")
        return data.val()


data = read_from_db("appropriate")
loop = asyncio.get_event_loop()
result = loop.run_until_complete(data)

pprint.pprint(result)

# try:
#     x = db.child("users").child("b1016118").get()
# except Exception as error:
#     print("Error:", error)
# else:
#     print("Success")
#     pprint.pprint(x)
