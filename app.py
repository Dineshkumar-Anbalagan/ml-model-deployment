from flask import Flask, render_template, request
import price

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method == "POST":
        carat = request.form["carat"]
        x, y, z = request.form["x"], request.form["y"], request.form["z"]
        price_pred = price.price_prediction(carat, x, y, z)
        
    return render_template("index.html", mpred = price_pred[0])

# @app.route("/submit", methods = ["POST"])
# def submit():
#     # html --> .py
#     if request.method == "POST":
#         name = request.form["username"]
    
#     # .py --> html
#     return render_template("submit.html", n = name)

if __name__ == "__main__":
    app.run(debug = True)