from secrets import Connect
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    connection = Connect.get_connection()
    db = connection.sirups_information
    sirups = db.sirups
    records = sirups.find()
    return render_template('index.html', records=records)
