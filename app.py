from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['DEBUG'] = True

@app.route('/getResponse', methods=['GET', 'POST'])
def chatbot():
    file = request.files['file']  
    print(file)
    file.save("test.wav")

    return 'Hello World!'
