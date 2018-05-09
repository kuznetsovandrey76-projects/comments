from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
# pgAdmin 3
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/nameDB'
# Heroku
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mcjjfkahcjovvg:cae8cb2dbae4fd3c5ac559abdbde638127fbae734f25f9a71588e49b5c5b5d45@ec2-54-75-246-50.eu-west-1.compute.amazonaws.com:5432/ddhr464rkg59r6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	comment = db.Column(db.String(200))

@app.route('/')
def index():
	result = Comments.query.all()
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

if __name__ == '__main__':
	app.run(debug=True)