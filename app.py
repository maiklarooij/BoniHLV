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
    clusters = {'Cluster 1': {'numbers': [19, 29, 35], 'desc': 'Frisdrank, bier en houdbare melk', 'time': 90},
                'Cluster 2': {'numbers': [1, 2, 15, 16, 18], 'desc': 'Koek, snoep, koffie en thee', 'time': 60}, 
                'Cluster 3': {'numbers': [5, 14, 23, 24, 25, 26, 28, 30], 'desc': 'Cosmetica, dierenvoeding en wasmiddel', 'time': 60},
                'Cluster 4': {'numbers': [3, 4, 9, 10, 11, 12, 36], 'desc': 'Potgroente, sauzen, conimex en eieren', 'time': 60},
                'Cluster 5': {'numbers': [7, 8, 13, 17, 20, 49], 'desc': 'Chips, wijn, ontbijt en afbakbrood', 'time': 60}}

    totals = {}
    for cluster in clusters:
        colli = df[df['Nummer'].isin(clusters[cluster]['numbers'])]['Colli'].map(lambda x: int(x)).sum()
        time = {'hours': "{:02d}".format(int(colli / clusters[cluster]['time'])), 
                'minutes': "{:02d}".format(int(((colli % clusters[cluster]['time']) / 1.5))) if cluster == 'Cluster 1' else "{:02d}".format(colli % clusters[cluster]['time']) }
        totals[cluster] = {'colli': colli, 'time': time, 'desc': clusters[cluster]['desc']}

    grandtotal = sum([totals[cluster]['colli'] for cluster in totals])
    return render_template("result.html", clusters=totals, grandtotal=grandtotal)
