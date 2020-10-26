# imports list for this project
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# App Instance and MongoDB configuration
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


def is_valid_id(id, model):
    """
    Function to verify that a the
    project or category id is valid
    else a 404 page is being showed.
    """
    try:
        model.find_one({"_id": ObjectId(id)})
        return True
    except:
        return False

# Routes


@app.route("/")
@app.route("/index")
def index():
    """
    This is the homepage of the site with primariy static content
    """
    return render_template("index.html")


@app.route("/get_projects")
def get_projects():
    """
    List of all projects created on the DB
    - All users have read access to the projects
    - Registered users can create projects
    - Project owners can edit and delete their own projects.
    """
    projects = list(mongo.db.projects.find())
    return render_template("projects.html", projects=projects)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Option to search projects based on index set
    to project name and description - the solution
    is from tutorial video for Task MAnager
    """
    query = request.form.get("query")
    projects = list(mongo.db.projects.find({"$text": {"$search": query}}))
    return render_template("projects.html", projects=projects)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registration page for user to register their charity.
    Checks if :
    - if username allready exist
    - if registration was saved
    - shows flash message if username already taken
    - shows flash message if registreation successful
    - hashes the password to the database
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "danger")
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
        flash("Registration Successful!", "success")
        return redirect(url_for("index", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Login page for user log in
    Checks if :
    - if username exists in DE
    - if registration was saved
    - shows flash message if username or password incorrect
    - shows flash message to welcome user
    - ensures hashed password matches user input
    """
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
                    request.form.get("username")), "success")
                return redirect(url_for("index", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password", "danger")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Profile page for logged in user
    Currently hidden to user requires UI/UX review
    - Get's the session user's username from DB
    """
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Link in navigation to log user out
    and remove their session cookie
    """
    # remove user from session cookie
    flash("You have been successfully logged out", "success")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/create_project", methods=["GET", "POST"])
def create_project():
    """
    Registered user can create a project by
    completing a form. Project categories can be
    selected by drop down
    """
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        project = {
            "project_category_name": request.form.get("project_category_name"),
            "project_name": request.form.get("project_name"),
            "project_overview": request.form.get("project_overview"),
            "project_description": request.form.get("project_description"),
            "project_img_url": request.form.get("project_img_url"),
            "is_urgent": is_urgent,
            "project_date": request.form.get("project_date"),
            "created_by": session["user"]
        }
        mongo.db.projects.insert_one(project)
        flash("Project Successfully Added", "success")
        return redirect(url_for("get_projects"))

    categories = mongo.db.project_categories.find().sort(
        "project_category_name", 1)
    return render_template("create_project.html", categories=categories)


@app.route("/project_detail/<project_id>", methods=["GET", "POST"])
def project_detail(project_id):
    """
    Detail page to surface the project
    information to the site visitor
    Error handling in place to check for valid id
    """
    if is_valid_id(project_id, mongo.db.projects):
        if request.method == "POST":
            is_urgent = "on" if request.form.get("is_urgent") else "off"
            project = {
                "project_category_name": request.form.get(
                    "project_category_name"),
                "project_name": request.form.get("project_name"),
                "project_overview": request.form.get("project_overview"),
                "project_description": request.form.get("project_description"),
                "project_img_url": request.form.get("project_img_url"),
                "is_urgent": is_urgent,
                "project_date": request.form.get("project_date"),
                "created_by": session["user"]
            }

        project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
        categories = mongo.db.project_categories.find().sort(
            "project_category_name", 1)
        return render_template(
            "project_detail.html", project=project, categories=categories)

    else:
        return render_template("404.html")


@app.route("/edit_project/<project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    """
    The creator of an project has the
    ability to edit and update their project.
    Error handling in place to check for valid id
    """
    if is_valid_id(project_id, mongo.db.projects):
        if request.method == "POST":
            is_urgent = "on" if request.form.get("is_urgent") else "off"
            edit = {
                "project_category_name": request.form.get(
                    "project_category_name"),
                "project_name": request.form.get("project_name"),
                "project_overview": request.form.get("project_overview"),
                "project_description": request.form.get("project_description"),
                "project_img_url": request.form.get("project_img_url"),
                "is_urgent": is_urgent,
                "project_date": request.form.get("project_date"),
                "created_by": session["user"]
            }
            mongo.db.projects.update({"_id": ObjectId(project_id)}, edit)
            flash("Project Successfully Updated", "success")
            return redirect(url_for("get_projects"))

        project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
        categories = mongo.db.project_categories.find().sort(
            "project_category_name", 1)
        return render_template(
            "edit_project.html", project=project, categories=categories)
    else:
        return render_template("404.html")


@app.route("/delete_project/<project_id>")
def delete_project(project_id):
    """
    The creator of an project has the
    ability to delete their project.
    Error handling in place to check for valid id
    """
    if is_valid_id(project_id, mongo.db.projects):
        mongo.db.projects.remove({"_id": ObjectId(project_id)})
        flash("Project Complete", "success")
        return redirect(url_for("get_projects"))
    else:
        return render_template("404.html")


@app.route("/get_categories")
def get_categories():
    """
    List of all projects created on the DB
    - Only visible to the username == admin
    - admin user can view all categories
    - adminuser can add, edit and delete categories.
    """
    categories = list(mongo.db.project_categories.find().sort(
        "project_category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/create_category", methods=["GET", "POST"])
def create_category():
    """
    Admin user can create a new category
    by filling out short form.
    """
    if request.method == "POST":
        category = {
            "project_category_name": request.form.get("project_category_name")
        }
        mongo.db.project_categories.insert_one(category)
        flash("New Category Successfully Added", "success")
        return redirect(url_for("get_categories"))

    return render_template("create_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Admin user can edit any category
    Error handling in place to check for valid id
    """
    if is_valid_id(category_id, mongo.db.category_id):
        if request.method == "POST":
            submit = {
                "project_category_name": request.form.get(
                    "project_category_name")
            }
            mongo.db.project_categories.update(
                {"_id": ObjectId(category_id)}, submit)
            flash("Category Successfully Updated", "success")
            return redirect(url_for("get_categories"))

        category = mongo.db.category_id.find_one(
            {"_id": ObjectId(category_id)})
        return render_template("edit_category.html", category=category)
    else:
        return render_template("404.html")


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Admin user can delete any category
    Error handling in place to check for valid id
    """
    if is_valid_id(category_id, mongo.db.category_id):
        mongo.db.project_categories.remove({"_id": ObjectId(category_id)})
        flash("Category Successfully Deleted", "success")
        return redirect(url_for("get_categories"))
    else:
        return render_template("404.html")


"""Error handling
    - Set up error handling leveraging inbuilt flask funtionality
    - reference -https://www.geeksforgeeks.org/python-404-
    error-handling-in-flask/#:~:text=A%20404%20Error%20is%20showed,the%20default%20Ugly%20Error%20page.
"""


# Error 403 handler route
# app name
@app.errorhandler(403)
# inbuilt function which takes error as parameter
def forbidden(e):
    # defining function
    return render_template('403.html'), 403


# Error 404 handler route
@app.errorhandler(404)
def page_not_found(e):

    return render_template('404.html'), 404


# Error 500 handler route
@app.errorhandler(500)
def server_error(e):

    return render_template('500.html'), 500


# To run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
