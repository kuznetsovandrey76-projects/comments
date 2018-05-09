from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
# если используешь pgAdmin 3
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/nameDB'
# если используешь Heroku
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hxeqjnnqpawpvd:da95269ab4f16bd45f511569568d791c6d491671ddb216c809701632eced90cb@ec2-54-247-89-189.eu-west-1.compute.amazonaws.com:5432/dc4dqg53di349k'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	comment = db.Column(db.String(200))

# Главная страница, в result загружается база данных
@app.route('/')
def index():
	result = Comments.query.all()
	result.reverse() # Обратный порядок
	return render_template('index.html', result=result)

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']

	signature = Comments(name=name, comment=comment)
	db.session.add(signature)
	db.session.commit()

	return redirect(url_for('index'))

# Включать для удаления постов (Удаляю по id записи)
@app.route('/delete/<string:id>')
def delete(id):
	result = Comments.query.filter_by(id=id).first()
	db.session.delete(result)
	db.session.commit()

	return redirect(url_for('index'))

# Дополнительно
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
	app.run(debug=True)