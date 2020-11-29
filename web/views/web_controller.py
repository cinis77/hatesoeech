import logging

from flask import escape, render_template, Blueprint, request, jsonify

from app.classifier import Classifier

web_controller = Blueprint('web_controller', __name__)
logger = logging.getLogger(__name__)

cl = Classifier.getInstance()


@web_controller.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@web_controller.route('/text', methods=['POST'])
def analyze():
    if request.data is None:
        return "Tekstas yra privalomas", 400

    if len(request.data) < 5:
        return "Tekstas turi būti ilgesnis", 400

    if len(request.data) > 10000:
        return "Tekstas per ilgas", 400

    text = escape(request.data.decode('UTF-8'))
    results = cl.check(text)
    return jsonify({"prediction": results.pred, "score": results.score}), 200
