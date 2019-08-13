from flask import Flask, jsonify, request, make_response
from flask_restful import abort, Api, Resource
import meta
import numpy as np
from database import Database
# import os
# import sys
# import sqlalchemy
# from flask_restful import reqparse

db = Database()
app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False


# schema = {
#    "type" : "object",
#    "properties" : {
#        "dna" : {"type" : "numpy.ndarray"}
#    },
# }


# Stats
# GET method, returns a JSON file containing:
# - Number of Unique Human DNA
# - Number of Unique Metahuman DNA
# - ratio of Metahuman in the overall population for all calls to /metahuman

class Stats(Resource):

    def get(self):
        
        results = db.fetchStats()
        
        ishuman = results[0]
        ismeta = results[1]
        ratio = results[2]
        
        message = {'unique_human_dna': ishuman, 
                   'unique_metahuman_dna': ismeta, 
                   'ratio': ratio}
        
        return make_response(jsonify(message), 200) 


# MetaHUman
# receives json with a dna sample via post
# returns 200 if the DNA is Metahuman
# returns 403 if the DNA is Human
class MetaHuman(Resource):

    def post(self):

        try:
            # imports json
            json_data = request.get_json(force=True)

            # gets dna and validates the data: NXN and all letters
            dna = np.array(json_data['dna'])
            dna_arr = np.array([list(line) for line in dna])
            if (len(dna_arr.shape) == 2
                and dna_arr.shape[0] == dna_arr.shape[1]
                    and all(ch.isalpha() for ch in dna) is True):

                eval_meta = meta.ismeta(dna)

                # save dna in db
                db.saveData(dna, eval_meta)
                if eval_meta is True:
                    message = {'message': 'DNA is Metahuman'}
                    return make_response(jsonify(message), 200)
                else:
                    message = {'message': 'DNA is Human'}
                    return make_response(jsonify(message), 403)
            else:
                return {'message': 'dna key has the wrong format'}

        except BaseException as e:

            print('ERROR:' + str(e))
            abort(400, message=str(e))


# Api resource routing
api.add_resource(MetaHuman, '/metahuman')
api.add_resource(Stats, '/stats')


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)
