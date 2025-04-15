from flask import Blueprint, request, render_template

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/calculate", methods=["POST"])
def calculate():
    try:
        a = float(request.form["a"])
        b = float(request.form["b"])
        operation = request.form["operation"]

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            result = a / b if b != 0 else "Ошибка: деление на ноль"
        else:
            result = "Недопустимая операция"

        return render_template("index.html", result=result)

    except Exception as e:
        return f"Ошибка: {e}", 400
