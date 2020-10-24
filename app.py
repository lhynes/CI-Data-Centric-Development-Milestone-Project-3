import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_projects")
def get_projects():
    projects = mongo.db.projects.find()
    return render_template("projects.html", projects=projects)
    

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    projects = list(mongo.db.projects.find({"$text": {"$search": query}}))
    return render_template("projects.html", projects=projects)
    

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "charity_overview": request.form.get("charity_overview").lower(),
            "charity_registration_number": request.form.get(
                "charity_registration_number").lower(),
            "charity_website": request.form.get("charity_website"),
            "charity_logo": request.form.get("charity_logo"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

         # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")
    

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]}) # removed ["username"] from end and will show on profile page
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/create_project", methods=["GET", "POST"])
def create_project():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        project = {
            "project_category_name": request.form.get("project_category_name"),
            "project_name": request.form.get("project_name"),
            "task_description": request.form.get("task_description"),
            "project_img_url": request.form.get("project_img_url"),
            "is_urgent": is_urgent,
            "project_date": request.form.get("project_date"),
            "created_by": session["user"]
        }
        mongo.db.projects.insert_one(project)
        flash("Project Successfully Added")
        return redirect(url_for("get_projects"))

    categories = mongo.db.project_categories.find().sort("project_category_name", 1)
    return render_template("create_project.html", categories=categories)


@app.route("/edit_project/<project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        edit = {
            "project_category_name": request.form.get("project_category_name"),
            "project_name": request.form.get("project_name"),
            "project_description": request.form.get("project_description"),
            "project_img_url": request.form.get("project_img_url"),
            "is_urgent": is_urgent,
            "project_date": request.form.get("project_date"),
            "created_by": session["user"]
        }
        mongo.db.projects.update({"_id": ObjectId(project_id)}, edit)
        flash("Project Successfully Updated")
        return redirect(url_for("get_projects"))

    project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
    categories = mongo.db.project_categories.find().sort("project_category_name", 1)
    return render_template("edit_project.html", project=project, categories=categories)


@app.route("/delete_project/<project_id>")
def delete_project(project_id):
    mongo.db.projects.remove({"_id": ObjectId(project_id)})
    flash("This Project is now complete")
    return redirect(url_for("get_projects"))

@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.project_categories.find().sort("project_category_name", 1))
    return render_template("categories.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)