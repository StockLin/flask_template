from flask import Blueprint, request, render_template, jsonify
from apps.shares_resturn.services.calc import Calculator

shares_return_bp = Blueprint('shares_return', __name__)


@shares_return_bp.route("/", methods=['GET'])
def index():
    try:
        return render_template('shares_return/index.html')

    except Exception as e:
        raise e

# 依照需求往下新增
@shares_return_bp.route("add", methods=['POST'])
def add():
    try:
        response = "Failed!"

        if request.method == 'POST':
            data = request.get_json()

            if 'x' in data.keys() and 'y' in data.keys():
                x = data['x']
                y = data['y']

                calc = Calculator()

                result = calc.add(x, y)

                response = {
                    "status":"success", 
                    "data":result
                }
            
        return jsonify(response)

    except Exception as e:
        raise e