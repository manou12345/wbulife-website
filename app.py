from flask import Flask, render_template

app = Flask(__name__)

CLASSES = [
  {
    'id': 1,
    'name': 'Intermediate Algebra'
  },
    {
    'id': 2,
    'name': 'College Algebra'
  },
    {
    'id': 3,
    'name': 'Calculus 1'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        classs = CLASSES)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
