from flask import Flask

# Declarando las variables
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola 2687386'