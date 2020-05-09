import os

from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

print(os.getenv("DATABASE_URL"))
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

print("hurz1")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        error = ""
        return render_template("register.html")
    if request.method == "POST":
        error = ""
        email = request.form.get("email")
        password0 = request.form.get("password")
        password1 = request.form.get("passwordRepeat")
        if len(email) < 5 or len(password0) < 8:
            error = "Either email or password length do not suffice (email has to be greater than 5 and password has to contain a minimum of 8 words)"
            print(error)
        print("hurz")
        if not password0 == password1:
            error = "Passwords do not match!"
            print(password0)
            print(password1)
            print(error)
        if error == "":
            db.execute("insert into accounts (email, passwd) values (:email, :password)", {"email": email, "password": password0})
            db.commit()
        print(f"Hallo {error}")
    return render_template("register.html", error=error)

@app.route("/login", methods=["POST", "GET"])
def login():
    error = ""
    email = request.form.get("email")
    password = request.form.get("password")
    if db.execute("select * from accounts where email=:email and passwd=:password", {"email": email, "password": password}).rowcount == 0:
        error = "Your email or passord is invalid"
        return render_template("index.html", error=error)
    else:
        userID = db.execute("select id from accounts where email=:email and passwd=:password", {"email": email, "password": password}).fetchone()
        return redirect(f"/account/{userID[0]}")

@app.route("/account/<user_id>", methods=["POST", "GET"])
def account(user_id=None):
    print(f"user_id:{user_id}")
    histories = db.execute("select id, amount from transactions where account_id=:userID", {"userID": user_id}).fetchall()
    return render_template("account.html", histories=histories, userID=user_id)

@app.route("/transaction", methods=["POST"])
def transaction():
    amount = request.form.get("amount")
    amount = int(amount)
    userID = request.form.get("userID")
    print(userID)
    histories = db.execute("select id, amount from transactions where account_id=:userID", {"userID": userID}).fetchall()
    if amount <= 0:
        error = "invalid amount"
        return render_template("account.html", histories=histories, userID=userID, error=error)
    else:
        db.execute("insert into transactions (account_id, amount) values (:userID, :amount)", {"userID": userID, "amount": amount})
        db.commit()
    return redirect(f"/account/{userID}")