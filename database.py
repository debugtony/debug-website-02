import os

from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)
def load_jobs_from_db():
  with engine.connect() as conn:
    query = text("SELECT * FROM jobs")
    result = conn.execute(query)  # Execute the query
    jobs = result.fetchall()
    return jobs

