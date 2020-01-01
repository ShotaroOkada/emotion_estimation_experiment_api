from flask import request
from flask_restful import Resource
from src.adapters.controller.user.post_user import post_user
from src.adapters.controller.bad_evaluation_text.get_bad_evaluation_text import get_bad_evaluation_text
from src.adapters.controller.emotion.get_emotion import get_emotion
from src.adapters.controller.evaluation.post_evaluation import post_evaluation


class Default(Resource):
    def get(self):
        return 'emotion_estimation_app'


class User(Resource):
    def post(self):
        user_id = request.headers['user_id']
        return post_user(user_id)


class BadEvaluationText(Resource):
    def get(self):
        user_id = request.headers['user_id']
        print(user_id)
        return get_bad_evaluation_text(user_id)


class Emotion(Resource):
    def get(self):
        user_id = request.headers['user_id']
        text = request.args['text']
        return get_emotion(user_id, text)


class Evaluation(Resource):
    def post(self):
        user_id = request.headers['user_id']
        evaluation = request.args['evaluation']
        return post_evaluation(user_id, evaluation)
