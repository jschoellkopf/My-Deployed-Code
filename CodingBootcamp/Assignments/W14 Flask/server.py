from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # "/" means http://127.0.0.1:5001
def home():
    print("print statements appear in the terminal")
    return render_template("home.html")

@app.route("/dojo")
def dojo():
    return render_template("dojo.html")

@app.route("/say/hi/<string:name>")
def say_hi(name):
    print(name)
    return render_template("say_hi.html", first_name = name)

@app.route("/repeat/<int:num>/<string:word>")
def repeat(num,word):
    return render_template("repeat.html", num = num, word = word)

# @app.route("/repeat/<int:num>/<string:word>")
# def repeat(num,word):
#   output = ''
#   for i in range(num):
#       output += f"<p>{word}</p>"
#   return output

@app.route('/<path:path>')
def catch_all(path):
    # returns a 200 (not a 404) with the following contents:
    return 'Sorry! No response. Try again.\n'

if __name__ == "__main__":
    app.run(debug=True,port=5001)