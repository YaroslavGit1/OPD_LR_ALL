from flask import Flask, render_template, request
import math

app = Flask(__name__)

exchange_rates = {
    "USD": 1.0,      # Базовая валюта
    "EUR": 0.94,     # Примерный курс: 1 USD ~ 0.94 EUR
    "RUB": 90.0,     # Примерный курс: 1 USD ~ 90 RUB
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates:
        raise ValueError(f"Валюта {from_currency} не поддерживается")

    if to_currency not in exchange_rates:
        raise ValueError(f"Валюта {to_currency} не поддерживается")

    if amount < 0:
        raise ValueError("Сумма для конвертации не может быть отрицательной")

    base_amount = amount / exchange_rates[from_currency]     
    converted = base_amount * exchange_rates[to_currency]     
    return converted

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            # Проверяем, все ли поля формы пришли
            if not all(key in request.form for key in ["amount", "from_currency", "to_currency"]):
                error = "Ошибка"
            else:
                amount_str = request.form.get("amount")
                from_currency = request.form.get("from_currency")
                to_currency = request.form.get("to_currency")

                try:
                    amount = float(amount_str)
                except ValueError:
                    error = "Ошибка"
                    raise

                # Выполняем конвертацию
                converted_value = convert_currency(amount, from_currency, to_currency)
                result = round(converted_value, 2)  # Округляем до 2 знаков

        except Exception as e:
            if not error:
                error = f"Ошибка: {str(e)}"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)

