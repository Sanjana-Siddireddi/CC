pip install Flask

____________________

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
	return 'Hello World from Google App Engine (Python)!'
if __name__ == '__main__':
	app.run()

__________________________


from flask import Flask
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def time():
        return "Current Date and Time: " + str(datetime.now())
if __name__ == '__main__':
        app.run(port=8080)
