from flask import Flask, request, jsonify
from expsys import GuessWho
import threading

app = Flask(__name__)
app.debug = True
gw = GuessWho()

def thread_game(is_woman):
    gw.reset(is_woman=is_woman)
    gw.run()

"""
'1.- ¿Tu docente es mujer?'
First question ALWAYS
"""

@app.route('/startGame', methods=['POST'])
def startGame():
    data = request.get_json()
    game = threading.Thread(target=thread_game, args=(data['answer'],))
    game.start()
    return jsonify({'question': '1.- ¿Tu docente es mujer?'}), 200

@app.route('/answerQuestion', methods=['POST'])
def answerQuestion():
    data = request.get_json()
    # global selectedAnswerFromUser
    # selectedAnswerFromUser = data['answer']
    return jsonify(data), 200

print(dir(gw))

if __name__ == '__main__':
    app.run(port=5000, host='localhost')