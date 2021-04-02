from flask import Flask, render_template, request

from Utils.Arabic2Roman import *

Flask_App = Flask(__name__)  # Creating our Flask Instance


@Flask_App.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@Flask_App.route('/', methods=['POST'])
def operation_result():

    first_input = request.form['Input1']
    operation = request.form['operation']

    try:
        if operation == "A2R":
            input1 = float(first_input)
            result = arabic2roman(input1)
        else:
            input1 = first_input
            result = roman2arabic(input1)

        return render_template('home.html', input1=input1, operation=operation, result=result, calculation_success=True)

    except ValueError:
        return render_template('home.html', input1=first_input, operation=operation, result="Bad Input", calculation_success=False, error="Cannot perform the required numeric conversion with provided input")


if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()
