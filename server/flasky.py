from flask import Flask
from flask_restful import Resource, Api

# db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Watersports(Resource):
    def get(self):
        return {'justin is a ': 'get'}

    def post(self):
        return {'justin is a ': 'post'}


api.add_resource(Watersports, '/watersports')

if __name__ == '__main__':
    print("Starting to run...")
    app.run(port='9999')
    print("Stopping run!")
