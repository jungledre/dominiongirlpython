
from flask import Flask, render_template, url_for, send_from_directory, request
import os


print "hi"
from dominiongirl import give10, giveCoin, giveVict
print "again"

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        deck = ['dominion']
    elif request.method == 'POST':
        deck = request.form.getlist('deckchoice')
        print deck
    print request.form
    # deck=request.form['deckchoice']
    # print deck
    # return "Hello World!"
    print ' '.join(give10(deck))
    # return ' '.join(give10(deck))
    print ' '.join(giveCoin(deck))
    print ' '.join(giveVict(deck))
    return render_template("index.html",
        cards = give10(deck), 
        coin = giveCoin(deck),
    	vict = giveVict(deck))

@app.route('/bower_components/<path:filename>')
def bower_components(filename):
    print os.path.join(app.root_path, 'bower_components', filename)
    return send_from_directory(os.path.join(app.root_path, 'bower_components'), filename)

if __name__ == "__main__":
    app.debug = True
    app.run()