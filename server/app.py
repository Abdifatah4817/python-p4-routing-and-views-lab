from flask import Flask

app = Flask(__name__)

# 1️⃣ Homepage route
@app.route('/')
def home():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2️⃣ Print route
@app.route('/print/<parameter>')
def print_text(parameter):
    print(parameter)  # prints to console
    return parameter  # display raw string

# 3️⃣ Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    # plain text with newline, including final newline
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return numbers

# 4️⃣ Math route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Division by zero is not allowed'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'

    return str(result)

# Optional: run Flask app locally
if __name__ == '__main__':
    app.run(debug=True)
