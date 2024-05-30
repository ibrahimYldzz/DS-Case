import numpy as np
import pandas as pd
from flask import Flask, request, make_response, jsonify
import json
import pickle
from sklearn.ensemble import GradientBoostingClassifier

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=FutureWarning) 
warnings.filterwarnings("ignore", category=UserWarning)


def json_to_df(data_json):
    data_dict = eval(json.dumps(data_json))
    data_df = pd.DataFrame(data_dict, index=[0])
    return data_df


feat_names = ["no_of_dependents", "education", "self_employed",	"income_annum",	"loan_amount", "loan_term", "cibil_score",
              "residential_assets_value", "commercial_assets_value", "luxury_assets_value", "bank_asset_value"]


app = Flask(__name__)


@app.route('/is_alive', methods=['GET'])
def is_alive():
    return "Running"


@app.route('/is_approval', methods=['POST'])
def is_approval():
    if request.is_json:
        try:
            assert request.is_json, "Request should be in JSON Format"

            input_data = request.get_json()
            input_data = json_to_df(input_data)

            with open("./models/xgb_tuned.pkl", "rb") as f:
                model = pickle.load(f)

            pred = model.predict(input_data[feat_names])
            
            if pred[0]==1:
                result = "Approved"
            else:
                result = "Rejected"
            
            print("Result:", result)
            return jsonify({"result": result})
 
        except Exception as e:
            err_msg = "Unexpected error while processing request " + str(e)
            return make_response(err_msg, 500)


if __name__ == '__main__':
    app.run()