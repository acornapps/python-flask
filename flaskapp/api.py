from pyfiglet import Figlet
import os
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

font = Figlet(font="starwars")

class CreateUser(Resource):
    def get(self):
        return {'status': 'success'}

api.add_resource(CreateUser, '/user')


@app.route("/")
def main():
    # get the message from the environmental variable $MESSAGE
    # or fall back to the string "no message specified"
    message = os.getenv("MESSAGE", "no message specified")

    # render plain text nicely in HTML
    html_text = font.renderText(message)\
            .replace(" ","&nbsp;")\
            .replace(">","&gt;")\
            .replace("<","&lt;")\
            .replace("\n","<br>")

    # use a monospace font so everything lines up as expected
    return "<html><body style='font-family: mono;'>" + html_text + "<p><a href='/api/v1/1'>JSON-TEST</a></p></body></html>"

@app.route('/api/v1/<int:id>', methods = ['GET'])
def get_sensor(id):
    try:
        return jsonify({'status': 'success','id':id})
    except NoResultFound:
        return jsonify({"message": "could not be found."}), 400



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port=8080)