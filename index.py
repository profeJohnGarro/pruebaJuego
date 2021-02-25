from flask import Flask

app = Flask(__name__)

@app.route('/')
def Game():
    return ('http://localhost:63342/Wabe_Same_The_Game/index.html?_ijt=f1jq9livht21is904rphnfeeip')

if __name__ == '__main__':
    app.run(debug=True, port=4525)

