from flask import Flask
from flask_restful import Api
from src.drivers.flaskDriver.crud import Default, User, BadEvaluationText, Emotion, Evaluation

app = Flask(__name__)
api = Api(app)

api.add_resource(Default, '/')
api.add_resource(User, '/user')
api.add_resource(BadEvaluationText, '/bad_evaluation_text')
api.add_resource(Emotion, '/emotion')
api.add_resource(Evaluation, '/evaluation')

if __name__ == '__main__':
    app.run()
