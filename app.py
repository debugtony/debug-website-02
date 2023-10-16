from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine, text  # Import the necessary modules

app = Flask(__name__)

# Create the database engine
db_connection_string = "mysql+pymysql://wdkj02w44ki25gka17ev:pscale_pw_8d5YNVD0LthjtvqdjbXNm3bUbOeOXXTBwkeoGzO4iUj@aws.connect.psdb.cloud/careers_debug?charset=utf8mb4"
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)

# Function to load jobs from the database
def load_jobs_from_db():
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs")
        result = conn.execute(query)  # Execute the query
        jobs = result.fetchall()
    return jobs

@app.route("/")
def render_jobs():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name='Debug')

@app.route("/api/jobs")
def get_jobs():
    jobs = load_jobs_from_db()
    job_list = [dict(job) for job in jobs]
    return jsonify(job_list)

if __name__ == "__main__":
    app.run(debug=True)
