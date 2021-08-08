from flask import Flask, jsonify, request
from flask_cors import CORS
from torch.functional import split
from model_files.ml_predict import predict_plant, Network
import base64
from decouple import config


app = Flask("manglish_lyrics_generation")
CORS(app)


@app.route('/', methods=['POST'])
def predict():
    key_dict = request.get_json()
    image = key_dict["image"]
    imgdata = base64.b64decode(image)
    model = Network()
    vehicle = predict_plant(model, imgdata)
    response = {
        "result": vehicle,
    }
    response = jsonify(response)
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
