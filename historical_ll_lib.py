import datetime

# import sys, os
# sys.path.append(r"~/Documents/projects.git/airflow-etl/airflow_home/dags/src")

from src.di_historical_lease_loader import start_run
from src.di_historical_lease_loader import DrillingInfo
from src.di_historical_lease_loader import Database
from src.di_historical_lease_loader import DatabaseMethods

def validation(start_date, end_date, state):
  #NOTE: checks if all the data is loaded to the target system from the source system
  start_run(state="NM")
  test_di = DrillingInfo()
  test_di = test_di.conn_to_di(test_di)
  start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
  end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
  extracted_rows = test_di.import_di_data(start_date=start_date, end_date = end_date, loc=state)
  extracted_rows = len(extracted_rows)

  test_db = DatabaseMethods()
  dbconn = test_db.connect_to_db()
  db_row_count = test_db.get_row_count(dbconn=dbconn, schema="source.di_nm_legal_leases")
  db_row_count = db_row_count["content"]

  if(extracted_rows == db_row_count):
    print("queried from di: "+str(extracted_rows)+" queried from db: "+str(db_row_count))
  else:
    raise AssertionError(str(extracted_rows)+" and "+str(db_row_count)+" are not equal")

def get_db_rows():
  test_db = DatabaseMethods()
  dbconn = test_db.connect_to_db()
  db_row_count = test_db.get_row_count(dbconn=dbconn, schema="source.di_nm_legal_leases")
  db_row_count = db_row_count["content"]
  return db_row_count

def get_di_rows(start_date, end_date, state):
  start_run(state="NM")
  test_di = DrillingInfo()
  test_di = test_di.conn_to_di(test_di)
  start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
  end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
  extracted_rows = test_di.import_di_data(start_date=start_date, end_date = end_date, loc=state)
  extracted_rows = len(extracted_rows)
  return extracted_rows

def testone():
  return 1

def testtwo():
  return 1