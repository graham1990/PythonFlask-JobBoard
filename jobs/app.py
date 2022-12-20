from flask import Flask, render_template, g
import sqlite3

PATH = 'db/jobs.sqlite'

app = Flask(__name__)


def open_connection():
    connection = g.getattr('_connection', None)
    if connection is None:
        connection = sqlite3.connect(PATH)
        g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection


def execute_sql():
    pass

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
