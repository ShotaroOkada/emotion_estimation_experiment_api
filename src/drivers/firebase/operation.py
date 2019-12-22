from app import db

try:
    db.child("evaluations").set(
        {
            "appropriate": {
                "id": "appropriate",
                "name": "適切",
                "score": 0
            },
            "inappropriate": {
                "id": "inappropriate",
                "name": "適切でない",
                "score": -0.1
            },
            "unknown": {
                "id": "unknown",
                "name": "わからない",
                "score": 0
            },
            "stronger": {
                "id": "stronger",
                "name": "より強い感情",
                "score": 0.1
            },
            "weaker": {
                "id": "weaker",
                "name": "より弱い感情",
                "score": -0.05
            }
        }
    )
except Exception as error:
    print("Error:", error)
else:
    print("Success")
