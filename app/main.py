from flask import Blueprint, request, jsonify

bp = Blueprint('main', __name__)

@bp.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    try:
        a = float(data.get("a"))
        b = float(data.get("b"))
        operation = data.get("operation")
    except Exception:
        return jsonify({"error": "Invalid input"}), 400

    result = None
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "Unknown operation"}), 400

    return jsonify({"result": result})
