from flask import Flask, request, jsonify
import pickle

from app.services import check_required_features
from app.services import get_data_of_features


# flask app
app = Flask(__name__)

# # loding the objects
# model = pickle.load(open(
#     'C:\\Users\\mo6tz\\Desktop\\ML project\\flask-app\\app\\models\\model.sav', 'rb'))
# enc = pickle.load(open(
#     'C:\\Users\\mo6tz\\Desktop\\ML project\\flask-app\\app\\models\\enc.sav', 'rb'))
model = pickle.load(open('../flask-app/app/models/model.sav'))
enc = pickle.load(open('../flask-app/app/models/enc.sav'))


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
            "prediction of value": model.predict(data)[0],
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
