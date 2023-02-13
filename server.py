from flask import Flask, request, json
from flask_restful import Resource, Api
from find_optimal_path import find_path

app = Flask('SpaceShip Rental')
api = Api(app)

class Spaceship(Resource):
    
    def post(self):
        if request.is_json:
            data = json.loads(request.data)
            try:
                path, income = find_path(data)
                return {"income": income, "path": path}
            except:
                return "Invalid request message.", 400
        else:
            return "Content type is not supported.", 415


api.add_resource(Spaceship, '/spaceship/optimize')

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
