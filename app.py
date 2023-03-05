from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

from chatty import *

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['DEBUG'] = True

@app.route('/getResponse', methods=['GET', 'POST'])
def chatbot():
    file = request.files['file']      
    file.save("test.wav")
    
    chat_history = request.form['history']
    #print(chat_history)

    chathistory = list(json.loads(chat_history))
    print(type(chathistory))
    response = respond_to_user(chathistory, "test.wav")

    print(response)

    return json.dumps(response)