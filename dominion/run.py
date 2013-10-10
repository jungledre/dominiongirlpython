from flask import Flask

from dominiongirl import give10

app = Flask(__name__)

#@app.route("/")
#def hello():
    # return "Hello World!"
#    print ' '.join(give10('Seaside'))
#    return ' '.join(give10('Seaside'))

if __name__ == "__main__":
    app.debug = True
    app.run()