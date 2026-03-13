from flask import Flask
app = Flask(__name__)

@app.route('/test')
def hello():
    return "<h1>Pipeline Funzionante! Let's GO!</h1><p>Versione 1.0</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)