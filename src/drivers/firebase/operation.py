from app import db
import pprint

try:
    x = db.child("users").child("b1016118").get()
except Exception as error:
    print("Error:", error)
else:
    print("Success")
    pprint.pprint(x)
