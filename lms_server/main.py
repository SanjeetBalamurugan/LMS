from flask import Flask
from .sql import SQL
import json

app = Flask(__name__)
scon = SQL(user='root', passwd='',host='127.0.0.1',database='LMS')

@app.route("/")
def main():
    rows = scon.query_books()
    return json.dumps(rows)
