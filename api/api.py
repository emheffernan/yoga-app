from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class Positions(Resource):
    def get(self):
        return {
            'positions': [
                'chivozna',
                'downward doggy',
                'sip tea',
                'sip more tea',
            ]
        }


api.add_resource(Positions, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
