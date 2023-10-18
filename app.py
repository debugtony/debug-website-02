from flask import Flask, jsonify, render_template

from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)



@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  job_list = [dict(job) for job in jobs]
  return jsonify(job_list)


@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('job_page.html', job=job)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)