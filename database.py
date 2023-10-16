from pymysql import cursors
from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://wdkj02w44ki25gka17ev:pscale_pw_8d5YNVD0LthjtvqdjbXNm3bUbOeOXXTBwkeoGzO4iUj@aws.connect.psdb.cloud/careers_debug?charset=utf8mb4"
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)

