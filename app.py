# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello world'

## import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, json, jsonify

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite",connect_args={'check_same_thread': False}) # use connect_args={'check_same_thread': False} to remove same thread errors
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# setting up flash location
app = Flask(__name__)

#setting up routes
@app.route("/")
def welcome():
    return(
    f"<h1>Welcome to the Climate Analysis API!</h1>"  # don't need <br/> when using h1,h2,h3 etc.
    f"<h2>Available Routes:</h2>"
    f"<a href=http://127.0.0.1:5000/api/v1.0/precipitation>/api/v1.0/precipitation<br/></a>" # removed "" for href to work
    f"<a href=http://127.0.0.1:5000/api/v1.0/stations>/api/v1.0/stations<br/>" #<br/> for next line, \n does not work
    f"<a href=http://127.0.0.1:5000/api/v1.0/tobs>/api/v1.0/tobs<br/>"
    f"<a href=http://127.0.0.1:5000/api/v1.0/temp/2017-06-01/2017-06-30>/api/v1.0/temp/start/end<br/>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == "USC00519281").\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps = temps)
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

if __name__ =="__main__":  #include this if you want to run the app with command: python3 app.py
    app.run(debug=True)