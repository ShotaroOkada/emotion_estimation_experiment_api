from app import db
import pprint
import asyncio
import time


async def read_from_db(key, sec):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, time.sleep, sec)
    try:
        data = db.child("evaluations").child(key).get()
    except Exception as error:
        print("error read: ", error)
    else:
        print("success read")
        return data.val()


async def main():
    data1 = asyncio.create_task(
        read_from_db("appropriate", 2)
    )
    data2 = asyncio.create_task(
        read_from_db("stronger", 2)
    )
    print(f"started at {time.strftime('%X')}")

    await data1
    await data2

    print(data1.result())
    print(data2.result())

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# try:
#     x = db.child("users").child("b1016118").get()
# except Exception as error:
#     print("Error:", error)
# else:
#     print("Success")
#     pprint.pprint(x)
