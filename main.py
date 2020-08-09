from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1 = request.args.get('A', default=0, type=int)
    value2 = request.args.get('B', default=0, type=int)
    result = value1 + value2
    return '%d \n' % result


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
        Error_msg = "There are error values in inputs, Please provide a list of values,for example 1,2,3,4"
        return Error_msg




if __name__ == "__main__":
    app.run()
