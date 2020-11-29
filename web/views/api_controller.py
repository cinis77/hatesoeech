import logging
from datetime import datetime
from flask import Blueprint, jsonify, request
from utils.config_parser import Config

from app.classifier import Classifier

logger = logging.getLogger(__name__)

api_controller = Blueprint('api_controller', __name__)
cl = Classifier.getInstance()


@api_controller.route('/ping', methods=['GET'])
def ping():
    return jsonify("pong", "%s" % datetime.now().isoformat())


@api_controller.route('/hs', methods=['POST'])
def post_hs():
    json = request.json
    if json is None:
        return "Bad request", 400

    if 'body' not in json:
        return "Body not found in json", 400

    text = str(json['body'])
    logger.debug("TEXT {}".format(text))
    results = cl.check(text)

    json_resp = {
        "classification": results.pred,
        "prediction": results.score
    }
    logger.debug("RESULT {}".format(json_resp))
    return jsonify(json_resp)
