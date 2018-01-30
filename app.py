from flask import Flask 	
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/projects")
def projects():
	return render_template('projects.html')

@app.route("/galleries")
def galleries():
	return render_template('galleries.html')

if __name__ == '__main__':
	app.run()