from flask import Flask, request
from faker import Faker
import csv
import requests

app = Flask(__name__)


@app.route("/")
def hello_mark():
    return "Hello, Mark!"


# Task 1
@app.route("/requirements/")
def requirements():
    with open("requirements.txt", "r") as file_requirements:
        text = ""
        for line in file_requirements:
            text += f"{line}<br>"
    return text


# Task 2
@app.route("/generate-users/")
def generate_users():
    fake = Faker()
    n = int(request.args.get("count", 100))
    text = ""
    for i in range(n):
        name = fake.name()
        email = str(name.replace(' ', '_')).lower() + '@gmail.com'
        text += f"{name}, {email}<br>"
        # text += f"{fake.name()}, {fake.email()}<br>"  # Второй вариант
    return text


# Task 3
@app.route("/mean/")
def average_data():
    with open('hw.csv', "r") as file:
        reader = csv.DictReader(file)
        total_weight = 0
        total_height = 0
        line_count = 0

        for row in reader:
            total_height += float(row.get(' "Height(Inches)"'))
            total_weight += float(row.get(' "Weight(Pounds)"'))
            line_count += 1

        mean_height = (total_height / line_count) * 2.54
        mean_weight = (total_weight / line_count) / 2.205
        return "Средний рост: {:.2f} см<br>Средний вес: {:.2f} кг".format(mean_height, mean_weight)


# Task 4
@app.route("/space/")
def space():
    response = requests.get("http://api.open-notify.org/astros.json")
    number_astronauts = response.json()["number"]
    return f'Количество космонавтов в настоящий момент: {number_astronauts}'


if __name__ == '__main__':
    app.run(debug=True)
