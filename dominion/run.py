from flask import Flask, render_template, url_for

print "hi"
from dominiongirl import give10, giveBasic

app = Flask(__name__)

@app.route("/")
def hello():
    # return "Hello World!"
    print ' '.join(give10('seaside'))
    # return ' '.join(give10('seaside'))
    print ' '.join(giveBasic('seaside'))
    return render_template("index.html",
        cards = give10('seaside'), 
        basic = giveBasic('seaside'))

if __name__ == "__main__":
    app.debug = True
