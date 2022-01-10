import os

from flask import Flask, jsonify, redirect, render_template, request, session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import pandas as pd

# Configure application
app = Flask(__name__)
app.config["SECRET_KEY"] = b'5\x95@j\xd7Z}\xd6\xfd\xafV\xfbU\xd6/\xf5'

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/", methods=["GET"])
def start():
    """ Main page where users can upload the .csv file to determine the 'colli's' of that day """

    # Render start template
    return render_template("start.html")

@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    file = request.files['bonicolli']
    
    header_list = ['Hoofdgroep', 'Omschrijving2', 'Boe', 'Bah', 'Nummer', 'Omschrijving', 'Colli']
    df = pd.read_csv(file, names=header_list).drop_duplicates()

    cluster1 = df[df['Nummer'].isin([19, 29, 35])]['Colli'].map(lambda x: int(x)).sum()
    cluster2 = df[df['Nummer'].isin([1, 2, 15, 16, 18])]['Colli'].map(lambda x: int(x)).sum()
    cluster3 = df[df['Nummer'].isin([5, 14, 23, 24, 25, 26, 28, 30])]['Colli'].map(lambda x: int(x)).sum()
    cluster4 = df[df['Nummer'].isin([3, 4, 9, 10, 11, 12, 36])]['Colli'].map(lambda x: int(x)).sum()
    cluster5 = df[df['Nummer'].isin([7, 8, 13, 17, 20, 49])]['Colli'].map(lambda x: int(x)).sum()
    total = cluster1 + cluster2 + cluster3 + cluster4 + cluster5
    clusters = {1: cluster1, 2: cluster2, 3: cluster3, 4: cluster4, 5: cluster5}

    return render_template("result.html", clusters=clusters, total=total)
