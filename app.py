from flask import Flask, request , jsonify;
import psycopg2;
import json;


class employee:
    def __init__(self, empid, empname):
        self.empid = empid
        self.empname = empname

app = Flask(__name__);

@app.route('/')
def greet():
    return "Hello python"

@app.route('/api/v1/timesheet/employee/all',methods=["GET"])
def hello():
     employees = [] 
     host = "postgresqldemo.postgres.database.azure.com"
     user = "csvadmin@postgresqldemo"
     dbname = "postgres"
     password = "admin@123"
     sslmode = "require"
     conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
     conn = psycopg2.connect(conn_string) 
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM empdata")
     rows = cursor.fetchall()
     return jsonify(rows);
            
if __name__ == '__main__':
    app.run('localhost',4449)
