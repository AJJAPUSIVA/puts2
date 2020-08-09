from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Usage;\n<Operation>?X=<Value1, Value2, ..., ValueN>\n"

if __name__ == "__main__":
    app.run()
