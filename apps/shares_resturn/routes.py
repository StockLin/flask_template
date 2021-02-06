from flask import Blueprint, request, render_template, jsonify
from apps.shares_resturn.services.calc import Calculator

shares_return_bp = Blueprint('shares_return', __name__)


@shares_return_bp.route("/", methods=['GET'])
def index():
    try:
        data = [
            {"k1":"AAA"},
            {"k1":"XYZ"},
            {"k1":"HAHA"}
        ]

        return render_template('shares_return/index.html', context=locals())

    except Exception as e:
        raise e

# 依照需求往下新增
@shares_return_bp.route("add", methods=['GET', 'POST'])
def add():
    try:

        if request.method == 'POST':
            response = {
                "status":"failed", 
                "data":""
            }

            data = request.get_json()
            print(data)

            if 'x' in data.keys() and 'y' in data.keys():
                x = int(data['x'])
                y = int(data['y'])

                calc = Calculator()

                result = calc.add(x, y)

                response = {
                    "status":"success", 
                    "data":result
                }
            
            return jsonify(response)

        return render_template('shares_return/calculator.html')

    except Exception as e:
        raise e