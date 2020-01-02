from src.drivers.firebase.app import db
import pprint


def push_user_evaluations(user_id, algo_name, text, evaluation_id):
    push_data = {
        "text": text,
        "evaluation_id": evaluation_id
    }
    try:
        db.child("users").child(user_id).child(
            algo_name + "_evaluations").push(push_data)
    except Exception as error:
        print("error push user evaluations:", error)
    else:
        print("success push user evaluations")
        pprint.pprint(push_data)
