from flask import Flask, request, render_template

webapp = Flask(__name__)


@webapp.get("/")
def home():
    return render_template("home.html",
                           title="Welcome")


if __name__ == "__main__":
    webapp.run()
