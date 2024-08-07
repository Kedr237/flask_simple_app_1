from flask import Flask, jsonify, redirect, render_template, request, url_for
from package.admin import process_person_info
from pg_db.delete import delete_person_info
from pg_db.extract import extract_persons
from pg_db.load import load_person_data
from pg_db.some_data import persons_data

app = Flask(__name__)


@app.get('/')
def get_home_page():
    data = extract_persons()
    return render_template('home.html', data=data)


@app.get('/admin/')
def admin():
    data = extract_persons()
    return render_template('admin.html', data=data, cur_page='admin')


@app.post('/person/')
def person_info():
    person_info = process_person_info(request)
    load_person_data([person_info])
    return redirect(url_for('admin'))


@app.delete('/person/<string:id>')
def delete_person(id):
    delete_person_info(id)
    return jsonify(success=True)


if __name__ == '__main__':
    load_person_data(persons_data)
    app.run(debug=True)
