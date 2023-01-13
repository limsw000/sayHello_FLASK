from flask import Flask, render_template, request, flash

app = Flask(__name__) # create a flask for the app
app.secret_key = "manbearpig_MUDMAN888"

# Select route for app, /hello is last part of url
@app.route("/hello") # Associate the route with a function
def index():
    flash("what's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"]) # When user press submit
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!") # name_input match with the one in index.html
    return render_template("index.html")