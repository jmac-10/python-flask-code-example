from flask import Flask, render_template, request
from wtforms import Form, StringField
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


class ReusableNameForm(Form):
    patient_name = StringField("Patient Name:")


@app.route('/search', methods=["GET", "POST"])
def search():
    form = ReusableNameForm(request.form)
    first_name = ''
    last_names = []

    if request.method == "POST":
        first_name = request.form["patient_name"].capitalize()
        patient_data = pd.read_csv("data/patient_tb.csv")
        last_names = patient_data[
            patient_data["PatientFirstName"] == first_name
        ]["PatientLastName"]
        last_names = list(pd.unique(last_names))

    data = {'first_name': first_name, 'last_names': last_names}

    return render_template("search.html", form=form, data=data)


@app.route('/search/detail', methods=["GET"])
def search_detail():
    last_name = request.args.get('lastname')
    first_name = request.args.get('firstname')
    patient_data = pd.read_csv("data/patient_tb.csv")
    patient_data = patient_data[
        (patient_data["PatientFirstName"] == first_name)
        & (patient_data["PatientLastName"] == last_name)
    ].to_html(classes='table table-striped', index=False)

    return render_template("search_detail.html", data=patient_data)


if __name__ == "__main__":
    app.run()
