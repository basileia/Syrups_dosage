from secrets import Connect
from flask import Flask, render_template
from werkzeug.exceptions import abort
from bson.objectid import ObjectId

app = Flask(__name__)


def get_db_connection():
    connection = Connect.get_connection()
    db = connection.sirups_information
    return db.sirups


def get_syrup(syrup_id):
    syrups = get_db_connection()
    syrup = syrups.find_one({"_id": ObjectId(syrup_id)})
    print(syrup)
    if syrup is None:
        abort(404)
    return syrup


@app.route('/')
def index():
    syrups = get_db_connection()
    records = syrups.find()  # seřadit podle abecedy
    return render_template('index.html', records=records)


@app.route('/<syrup_id>')
def syrup(syrup_id):
    syrup = get_syrup(syrup_id)
    return render_template('syrup.html', syrup=syrup)
