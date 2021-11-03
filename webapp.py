from flask import Flask, request, render_template

webapp = Flask(__name__)


@webapp.get("/")
def home():
    return render_template("home.html", title="Welcome")

@webapp.get("/about")
def about():
    return render_template("about.html", title="About me")

@webapp.get("/cv")
def mycv():
    return render_template("cv.html", title="My CV")

@webapp.get("/technologies")
def mycv():
    return render_template("technologies.html", title="Computing technologies")

@webapp.get("/interests")
def mycv():
    return render_template("interests.html", title="Personal interests")


if __name__ == "__main__":
    webapp.run()
