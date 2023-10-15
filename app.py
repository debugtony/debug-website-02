from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data anylist',
    'location': 'Berlin',
    'salary': '$10, 000'
  },
  {
    'id': 2,
    'title': 'Data scientist',
    'location': 'New york',
    'salary': '$12, 000'
  },
  {
    'id': 3,
    'title': 'Frotend engineer',
    'location': 'Remote',
    'salary': '$15, 000'
  },
  {
    'id': 4,
    'title': 'Backend engineer',
    'location': 'London',
    'salary': '$30, 000'
  }
  
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)



@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)