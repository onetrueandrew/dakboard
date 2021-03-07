import flask
import sys, os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/away', methods=['GET'])
def home():
    datetime1 = "away"
    file = 'away'
    with open(file,'w') as filewrite:
        filewrite.write(datetime1)
    return "200"

@app.route('/home', methods=['GET'])
def home2():
    datetime2 = "home"
    file = 'away'
    with open(file,'w') as filewrite:
        filewrite.write(datetime2)
    return "200"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
