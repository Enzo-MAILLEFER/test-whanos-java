from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return 'salut anas'

app.run(host='0.0.0.0', port=8080)