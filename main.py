from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>SGM-3007: Pipeline Funzionante!</h1><p>Versione 1.0</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)