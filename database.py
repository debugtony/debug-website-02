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


def load_job_from_db(id):
  with engine.connect() as conn:
      result = conn.execute(
          text("SELECT * FROM jobs WHERE id = :val").bindparams(val=id)
      )
      rows = result.all()

      if len(rows) == 0:
          return None
      else:
          # Convert the first row (which is a tuple) to a dictionary
          job_data = {}
          first_row = rows[0]  # Get the first row
          for i, key in enumerate(result.keys()):
              job_data[key] = first_row[i]
          return job_data





