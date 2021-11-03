import os
from flask import Flask, request, render_template

webapp = Flask(__name__)
numTechnologies = 0

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
def defaultTechnology():
    return technologies(1)

@webapp.get("/technologies/<index>")
def technologies(index):
    if (int(index) > numTechnologies): index = numTechnologies
    s = "technologies{id}.html"
    return render_template(s.format(id=index), title="Computing technologies")

@webapp.get("/interests")
def interests():
    return render_template("interests.html", title="Personal interests")


if __name__ == "__main__":
    files = os.listdir("./templates")
    for file in files:
        if file.startswith('technologies'):
            numTechnologies += 1
    webapp.run(debug=True)
