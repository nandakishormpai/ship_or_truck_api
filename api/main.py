from flask import Flask, jsonify, request
from flask_cors import CORS
from torch.functional import split
from model_files.ml_predict import predict_vehicle, Network
import base64
from decouple import config


app = Flask("ship_or_truck_api")
CORS(app)


@app.route('/', methods=['POST'])
def predict():
    key_dict = request.get_json()
    image = key_dict["image"]
    imgdata = base64.b64decode(image)
    model = Network()
    vehicle = predict_vehicle(model, imgdata)
    response = {
        "result": vehicle,
    }
    response = jsonify(response)
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
