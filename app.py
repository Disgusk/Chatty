from flask import Flask, request
from flask_cors import CORS, cross_origin

from chatty import *

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['DEBUG'] = True

@app.route('/getResponse', methods=['GET', 'POST'])
def chatbot():
    file = request.files['file']      
    file.save("test.wav")

    chathistory = setup_chat(1)
    response = respond_to_user(chathistory, "test.wav")

    print(response)

    return response