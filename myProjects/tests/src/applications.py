from flask import Flask, render_template, session, request
from calculator import square

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def index():
  result = 0
  error = ""
  if request.method == "POST":
    result = 0
    number = request.form.get("number")
    text = f"'{number}', Ist Typ: {type(number)}, Ist leer: {not number}, Ist eine Zahl: {number.isdigit()}"
    
    if not number:
      error = "Bitte eine Zahl eingeben"
    else:
      try:
        test = square(float(number))
        string = f"{number} squared is {test}"
        result = f"{string}!"
        history.append(string)
      except ValueError:
        error = "Please Type In A NUMBER!"
        result = "error"
  return render_template("index.html",result=result, history=history, error=error, text=text)

  