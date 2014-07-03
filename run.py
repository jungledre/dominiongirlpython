import logging
from flask import Flask, render_template, url_for, send_from_directory, request
import os

from dominiongirl import give10, giveCoin, giveVict

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        DECKS = ['dominion']
    elif request.method == 'POST':
        DECKS = request.form.getlist('deckchoice')
    logging.debug(request.form)
    logging.debug(' '.join(give10(DECKS)))
    logging.debug(' '.join(giveCoin(DECKS)))
    logging.debug(' '.join(giveVict(DECKS)))
    return render_template("index.html",
        cards = give10(DECKS),
        coin = giveCoin(DECKS),
        vict = giveVict(DECKS),
        decks = ' + '.join(DECKS))

@app.route('/bower_components/<path:filename>')
def bower_components(filename):
    return send_from_directory(os.path.join(app.root_path, 'bower_components'), filename)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)))
    app.run(host="0.0.0.0", debug=True, port=port)
