import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("postgres://hoxhmsgvomwfov:274ae0d3c75a6eb5dc4afe74e3551e6285ad7c25a56077941f254bd79b038275@ec2-18-210-51-239.compute-1.amazonaws.com:5432/d2t4ek219q5l6v"))
db = scoped_session(sessionmaker(bind = engine))

def main ():
  f = open("databases/csv/flights.csv")
  reader = csv.reader(f)
  for origin, destination, duration in reader:
    db.execute("INSERT INTO flights (origin,destination,duration) VALUES (:origin, :destination, :duration)", ("origin": origin ")