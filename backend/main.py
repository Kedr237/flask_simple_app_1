from flask import Flask, render_template
from pg_db.extract import extract_persons
from pg_db.load import load_person_data
from pg_db.some_data import persons_data

app = Flask(__name__)


@app.get('/')
def get_home_page():
    data = extract_persons()
    return render_template('home.html', data=data)


@app.get('/admin/')
def get_admin_page():
    return render_template('admin.html')


if __name__ == '__main__':
    load_person_data(persons_data)
    app.run()
