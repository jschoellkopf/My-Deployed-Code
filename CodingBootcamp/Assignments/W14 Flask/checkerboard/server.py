from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def default_checker():
    return render_template("index.html", col = 10, row = 10, color1 = "brown", color2 = "beige")

@app.route("/<int:row>")
def checker_row(row):
    return render_template("index.html", col = 10, row = row, color1 = "brown", color2 = "beige")

@app.route("/<int:col>/<int:row>")
def checker(col,row):
    return render_template("index.html", col = col, row = row, color1 = "brown", color2 = "beige")

@app.route("/<int:col>/<int:row>/<string:color1>/<string:color2>")
def checker_color(col,row,color1,color2):
    return render_template("index.html", col = col, row = row, color1 = color1, color2 = color2)

@app.route('/<path:path>')
def catch_all(path):
    # returns a 200 (not a 404) with the following contents:
    return 'Sorry! No response. Try again.\n'

if __name__ == "__main__":
    app.run(debug=True,port=5001)