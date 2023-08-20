from flask import Flask, request, jsonify
import pickle
import numpy as np
from app.services import check_required_features
from app.services import get_data_of_features


# flask app
app = Flask(__name__)

# loding the model
model = pickle.load(open('./models/model.sav'))
enc = pickle.load(open('./models/enc.sav'))


@app.route('/api/v1/single/prediction', methods=['POST'])
def single_prediction():
    """function to predict of single sample,
        it take data as an json format

    Returns:
        [response]: [contain the predict value]
    """

    try:
        data = request.get_json()
        check_required_features(data)
        data = [get_data_of_features(data)]
        data = enc.transform(data)

        response = {
            "status": 200,
            "prediction of value": np.expm1(model.predict(data)[0]),
        }
    except Exception as e:

        response = {
            "status": 400,
            "response": str(e)
        }

    return jsonify(response)


def create_app():
    """function to return Flask object

    Returns:
        [app]: [Flask object created]
    """
    return app
