from src.drivers.firebase.app import db


def read_evaluations():
    try:
        evaluations = db.child("evaluations").get()
    except Exception as error:
        print("error read evaluations:", error)
    else:
        print("success read evaluations")
        return evaluations
