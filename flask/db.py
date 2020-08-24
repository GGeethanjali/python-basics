from archana import flask_demo
from archana.flask_demo import jsonify
from sqlalchemy import create_engine

app = flask_demo.Flask(__name__)
app.config["DEBUG"] = True

vehicle_types = [
    {'id': 1,
     'type': 'aircraft'},
    {'id': 2,
     'type': 'spacecraft'},
    {'id': 3,
     'type': 'watercraft'}
]

def connect_db():
    db_connection_string = "postgresql://postgres:admin123@localhost:5432/maatram"
    return create_engine(db_connection_string)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to GoRide</h1>
<p>A ride hiring and offering app customised for your needs.</p>'''


@app.route('/vehicle-types', methods=['GET'])
def get_all_vehicle_types():
    vehicle_types_from_db = db.execute("SELECT * FROM go_ride.vehicle_types")
    formatted_result = [dict(row) for row in vehicle_types_from_db]
    return jsonify(formatted_result)
#     return jsonify(vehicle_types)

db = connect_db()
app.run()
