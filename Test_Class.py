
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from core import app, db

from models import Students


@app.route('/')
def show_all():
    return render_template('show_all.html', students=Students.query.all()) # or Students.query.filter_by(city='').all()


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = Students(request.form['name'], request.form['city'],
                               request.form['addr'], request.form['pin'])

            db.session.add(student)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
    app.run('localhost', 8000)