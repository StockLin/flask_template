from flask import Blueprint, request, render_template


shares_return_bp = Blueprint('shares_return', __name__)


@shares_return_bp.route("/", methods=['GET'])
def index():
    try:
        return render_template('shares_return/index.html')

    except Exception as e:
        raise e

# 依照需求往下新增
@shares_return_bp.route("/test", methods=['GET', 'POST'])
def ABCABC():
    try:
        return render_template('shares_return/index.html')

    except Exception as e:
        raise e