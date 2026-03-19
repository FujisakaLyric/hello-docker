from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', title = 'To-Do List')

@app.route('/about')
def about():
  name = '30 Days Of Python Programming'
  return render_template('about.html', name = name, title = 'About')

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(debug=True, host='0.0.0.0', port=port)