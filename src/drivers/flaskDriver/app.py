from flask import Flask, request
from src.adapters.controller.emotion.get_emotion import get_emotion
from src.adapters.controller.emotion.post_emotion import post_emotion
from src.adapters.controller.user.post_user import post_user
from src.adapters.controller.bad_evaluation_text.get_bad_evaluation_text import get_bad_evaluation_text

app = Flask(__name__)


@app.route('/')
def main():
    return 'emotion_estimation_app'


@app.route('/user', methods=['POST'])
def route_user():
    if request.method == 'POST':
        user_id = request.headers['user_id']
        post_user(user_id)


@app.route('/bad_evaluation_text')
def route_text():
    user_id = request.headers['user_id']
    get_bad_evaluation_text(user_id)


@app.route('/emotion', methods=['GET', 'POST'])
def route_emotion():
    if request.method == 'GET':
        user_id = request.headers['user_id']
        text = request.args['text']
        get_emotion(user_id, text)

    elif request.method == 'POST':
        user_id = request.headers['user_id']
        text = request.args['text']
        evaluation = request.args['evaluation']
        emotion_name = request.args['emotion_name']
        post_emotion(user_id, text, evaluation, emotion_name)


@app.route('/evaluation', methods=['POST'])
def route_evaluation():
    hoge


if __name__ == '__main__':
    app.run()
