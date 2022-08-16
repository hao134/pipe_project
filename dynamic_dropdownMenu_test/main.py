from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    state = db.Column(db.String(2))
    name = db.Column(db.String(50))


class Form(FlaskForm):
    state = SelectField("state", choices = [('CA', 'California'), ('NV', 'Nevada')])
    city = SelectField("city", choices=[])

@app.route("/", methods = ["GET", "POST"])
def index():
    form = Form()
    form.city.choices = [(city.id, city.name) for city in City.query.filter_by(state="NV").all()]

    if request.method == "POST":
        city = City.query.filter_by(id=form.city.data).first()
        return f"<h1> State: {form.state.data}, City: {city.name}</h1>"

    return render_template("index.html", form = form)


@app.route("/city/<state>")
def city(state):
    citites = City.query.filter_by(state=state).all()

    cityArray = []

    for city in citites:
        cityObj = {}
        cityObj["id"] = city.id
        cityObj["name"] = city.name
        cityArray.append(cityObj)
    return jsonify({"cities":cityArray})

# db.create_all()

if __name__ == "__main__":
    app.run(debug=True)