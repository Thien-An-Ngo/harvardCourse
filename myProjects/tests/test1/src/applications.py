import os

from flask import Flask, render_template, session, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/booker", methods=["GET", "POST"])
def booker():
    flights = []
    error = ""
    if request.method == "GET" or "POST":
        flights = db.execute("select * from flights")
    if request.method == "POST":
        try:
            flight_id = request.form.get("flightId")
            surname = request.form.get("surname")
            name = request.form.get("name")
            email = request.form.get("email")
            # Validation einbauen
            db.execute("insert into passengers (surname, name, email, flight_id) values (:surname, :name, :email, :flight_id)", 
                    {"surname": surname, "name": name, "email": email, "flight_id": flight_id})
            db.commit()
        except ValueError:
            error = "Please select a flight!"
    return render_template("booker.html", flights=flights, error=error)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/addFlight", methods=["GET", "POST"])
def addFlight():
    if request.method == "POST":
        origin = request.form.get("o")
        destination = request.form.get("dest")
        duration = request.form.get("dur")
        db.execute("insert into flights (origin, destination, duration) values (:origin, :destination, :duration)", 
                {"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes")
        db.commit()
    return render_template("addFlight.html")
