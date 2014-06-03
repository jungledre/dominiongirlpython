import logging
from flask import Flask, render_template, url_for, send_from_directory, request
import os

from dominiongirl import give10, giveCoin, giveVict

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        decks = ['dominion']
    elif request.method == 'POST':
        decks = request.form.getlist('deckchoice')
    logging.debug(request.form)
    logging.debug(' '.join(give10(decks)))
    logging.debug(' '.join(giveCoin(decks)))
    logging.debug(' '.join(giveVict(decks)))
    return render_template("index.html",
        cards = give10(deck),
        coin = giveCoin(deck),
        vict = giveVict(deck),
        decks = ', '.join(decks))

@app.route('/bower_components/<path:filename>')
def bower_components(filename):
    return send_from_directory(os.path.join(app.root_path, 'bower_components'), filename)

if __name__ == "__main__":
    app.debug = True
    app.run()
