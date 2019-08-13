# metahuman-api

## Getting Started
### what is this?
Web API in the path /metahuman that receives a JSON via POST with a dna sample and returns 
code 200 if the DNA is Metahuman or 403 if the DNA is Human.
In the path /stats returns a JSON file
with the Number of Unique Human DNA, Number of Unique Metahuman DNA and the ratio of
Metahuman in the overall population for all the calls made to the /metahuman path.


## Deployment
Clone the repo

$ git clone https://github.com/Victoriapm/metahuman-api.git

$ cd metahuman-api

Create the virtualenv

$ virtualenv venv

Install dependencies

$ pip3 install -r requirements.txt

Create the DB

CREATE TABLE DNA_SAMPLES (
   dna_array STRING[] PRIMARY KEY,
   ismeta BOOL NOT NULL
);

Run the app

$ python3 api.py


## Built With

- [Flask](https://palletsprojects.com/p/flask/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/quickstart.html#)
- Python 3.6

## Authors
- Victoria Perez Mola
