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
@app.route("/get_jobs")
def get_jobs():
    jobs = list(mongo.db.jobs.find())
    return render_template("jobs.html", jobs=jobs)


# User registration
@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        # Check to see if user already exists in MongoDB
        existing_user = mongo.db.staff.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This staff member already exists")
        # Redirects back to the same create account page
            return redirect(url_for('create_account'))

        create_account = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "role": request.form.get("role").lower()
        }
        mongo.db.staff.insert_one(create_account)

        # Add new staff account into session cookie
        session["staff"] = request.form.get("username").lower()
        flash("Staff members registration succesful")
    return render_template("create_account.html")


# User Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check to see if user already exists in MongoDB
        existing_user = mongo.db.staff.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check password matches the one stored in MongoDB
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome to the PLS Worklist System, {}".format(
                        request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Invalid password
                flash("Username and/or Password are Incorrect!")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Username and/or Password are Incorrect!")
            return redirect(url_for("login"))

    return render_template("login.html")    


# User Profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Retrieve the session users ursername from MongoDB
    username = mongo.db.staff.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove session cookie from user
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_job", methods=["GET", "POST"])
def add_job():
    if request.method == "POST":
        job_priority = "on" if request.form.get("job_priority") else "off"
        job = {
            "job_type_name": request.form.get("job_type_name"),
            "job_name": request.form.get("job_name"),
            "job_description": request.form.get("job_description"),
            "job_priority": job_priority,
            "job_due_date": request.form.get("job_due_date"),
            "created_by": session["user"]
        }
        mongo.db.jobs.insert_one(job)
        flash("New Job Added to System")
        return redirect(url_for("get_jobs"))

    job_type = mongo.db.job_type.find().sort("job_type_name", 1)
    return render_template("add_job.html", job_type=job_type )


@app.route("/edit_job/<job_id>", methods=["GET", "POST"])
def edit_job(job_id):
    job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
    job_type = mongo.db.job_type.find().sort("job_type_name", 1)
    return render_template("edit_job.html", job=job, job_type=job_type)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  