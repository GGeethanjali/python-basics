from archana import flask_demo
from archana.flask_demo import jsonify, request

app = flask_demo.Flask(__name__)
app.config["DEBUG"] = False

vehicle_types = [
    {'id': 1,
     'type': 'aircraft'},
    {'id': 2,
     'type': 'spacecraft'},
    {'id': 3,
     'type': 'watercraft'}
]

@app.route('/')
def home():
    user_id = request.args.get('id')
    return str(user_id)


@app.route('/vehicle-types/<path-param>', methods=['GET'])
def get_all_vehicle_types():
    return jsonify(vehicle_types)

app.run()


# jsonify
# debug mode
# without methods
