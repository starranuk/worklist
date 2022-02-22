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
    jobs = mongo.db.jobs.find()
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)    