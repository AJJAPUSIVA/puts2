from flask import Flask, request
import statistics

app = Flask(__name__)


def Inputs_method():
    try:
        inputs = request.args.get('X', type=str)
        inputs = inputs.split(',')
        values = []
        for value in inputs:
            value = float(value)
            values.append(value)
        return values
    except ValueError:
        Error_msg = "There are error values in inputs, Please provide a list of values,for example 1,2,3,4\n"
        return Error_msg


@app.route('/median')
def median():
    values = Inputs_method()
    if not type(values) is str:
        med = statistics.median(values)
        if med.is_integer():
            return str(int(med)) + ' \n'
        else:
            return str(float(round(med, 3))) + ' \n'
    else:
        return values


if __name__ == "__main__":
    app.run()
