from flask import Flask, jsonify, render_template, request

from database import add_application_to_db, load_job_from_db, load_jobs_from_db

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

@app.route("/job/<int:id>/apply", methods=["POST"])
def apply_to_job(id):
    full_name = request.form.get('full_name')
    email = request.form.get('email')
    linkdin_url = request.form.get('linkdin_url')
    education = request.form.get('education')
    work_experience = request.form.get('work_experience')
    resume_url = request.form.get('resume_url')
    job = load_job_from_db(id)

    data = {
        "full_name": full_name,
        "email": email,
        "linkdin_url": linkdin_url,
        "education": education,
        "work_experience": work_experience,
        "resume_url": resume_url
    }

    add_application_to_db(id, data)

    response_data = {
        "message": "Data received successfully",
        "full_name": full_name,
        "email": email,
        "linkdin_url": linkdin_url,
        "education": education,
        "work_experience": work_experience,
        "resume_url": resume_url
    }

    return render_template('application_submitted.html', application=response_data, job=job)





if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)