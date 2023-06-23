from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY']='key'

oxygen_level = 0
temprature_level = 0
hbpm_level = 0

class HealthForm(FlaskForm):
    oxygen = IntegerField("Oxygen", validators=[DataRequired()])
    temprature = IntegerField("temprature", validators=[DataRequired()])
    hbpm = IntegerField("Heart Beat Per Minute", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/', methods=["GET", "POST"])
def hello_world():
    form = HealthForm()
    if form.validate_on_submit():
        oxygen_level = form.oxygen.data
        temprature_level = form.temprature.data
        hbpm_level = form.hbpm.data

        if oxygen_level >= 95 and oxygen_level <= 100:
            oxygen_level_response = "Your oxygen level is balanced 🥳"
        elif oxygen_level >= 90 and oxygen_level <= 105:
            oxygen_level_response = "Your oxygen level is average 😐"
        else:
            oxygen_level_response = "RIP"

        if temprature_level >= 36.1 and temprature_level <= 37.2:
            temprature_level_response = "Your body temprature is normal"
        elif temprature_level >= 34 and temprature_level <= 39:
            temprature_level_response = "Consult a doctor ASAP!"
        else:
            temprature_level_response = "How are you even alive?!?!"

        if hbpm_level >= 60 and hbpm_level <= 100:
            hbpm_level_response = "Your hearbeat is in range"
        elif hbpm_level >= 25 and hbpm_level <=165:
            hbpm_level_response = "Consult a doctor ASAP!!!"
        else:
            hbpm_level_response = "You are a ghost!"

        sum = oxygen_level+hbpm_level+temprature_level

        if sum >= 190 and sum <= 237:
            final = "You are absolutely healthy"
        elif sum >= 170 and sum <= 270:
            final = "Your health is average!"
        else:
            final = "Make funeral arrangements ASAP! (and don't forget to call your relatives 😐 )"

        return render_template("index.html", form=form, olr = oxygen_level_response or None, tlr = temprature_level_response, hlr= hbpm_level_response, final = final)

    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)