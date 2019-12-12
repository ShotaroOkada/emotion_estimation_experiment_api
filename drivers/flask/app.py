from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def mainPage():
    return 'Hi!'


@app.route('/emotionParam', methods=['POST'])
def postEmotionParam():
    params = request.args
    return params


if __name__ == '__main__':
    app.run()
