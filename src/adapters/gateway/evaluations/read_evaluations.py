from src.drivers.firebase.app import db


def read_evaluations():
    try:
        response = db.child("evaluations").get()
    except Exception as error:
        print("error read evaluations:", error)
    else:
        evaluations = response.val()
        print("success read evaluations")
        return evaluations
