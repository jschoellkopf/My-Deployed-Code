from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def play1():
    return render_template("play.html", num = 3, color ="lightgray")

@app.route("/play/<int:num>")
def multiply(num):
    return render_template("play.html", num = num)

@app.route("/play/<int:num>/<color>")
def colored_boxes(num,color):
    return render_template("play.html", num = num, color = color)

@app.route('/<path:path>')
def catch_all(path):
    # returns a 200 (not a 404) with the following contents:
    return 'Hi Sorry! No response. Try again.\n'

if __name__ == "__main__":
    app.run(debug=True,port=5001)