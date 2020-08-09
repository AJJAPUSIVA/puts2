from flask import Flask, request
import statistics

app = Flask(__name__)


@app.route('/')
def index():
    return "Usage;\n<Operation>?X=<Value1, Value2, ..., ValueN>\n"


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


@app.route('/max')
def maximum():
    values = Inputs_method()
    if not type(values) is str:
        values.sort(reverse=True)
        if values[0].is_integer():
            return str(int(values[0])) + ' \n'
        else:
            return str(values[0]) + ' \n'
    else:
        return values


@app.route('/min')
def minimum():
    values = Inputs_method()
    if not type(values) is str:
        values.sort()
        if values[0].is_integer():
            return str(int(values[0])) + ' \n'
        else:
            return str(float(round(values[0], 1))) + ' \n'


@app.route('/average')
def average():
    values = Inputs_method()
    if not type(values) is str:
        avrg = statistics.mean(values)
        if avrg.is_integer():
            return str(int(avrg)) + ' \n'
        else:
            return str(float(round(avrg, 3))) + ' \n'
    else:
        return values


@app.route('/avg')
def avg():
    values = Inputs_method()
    if not type(values) is str:
        avrg = statistics.mean(values)
        if avrg.is_integer():
            return str(int(avrg)) + ' \n'
        else:
            return str(float(round(avrg, 3))) + ' \n'
    else:
        return values


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


@app.route('/mean')
def mean():
    values = Inputs_method()
    if not type(values) is str:
        avrg = statistics.mean(values)
        if avrg.is_integer():
            return str(int(avrg)) + ' \n'
        else:
            return str(float(round(avrg, 3))) + ' \n'


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
