import json

from eve import Eve
from flask import current_app
import requests

app = Eve()
app.config['DEBUG'] = True


def after_deleted_collections(item):
    current_app.data.driver.db['images'].remove({"collection": item['_id']}, multi=True)

app.on_deleted_item_collections += after_deleted_collections


@app.route("/networks/train/<network_id>", methods=['POST'])
def networks_train(network_id):
    operation = requests.post('http://neural_network/train/', {'network_id': network_id}).json()
    return json.dumps(operation)


@app.route("/networks/predict/<network_id>/<image_id>", methods=['POST'])
def networks_predict(network_id, image_id):
    result = requests.post('http://neural_network/predict/', {'network_id': network_id, 'image_id': image_id}).json()
    return json.dumps(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
