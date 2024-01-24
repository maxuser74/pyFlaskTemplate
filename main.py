import json

from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

which = True
img1 = ''
with open('1.svg', 'r') as file:
    for i in file:
        img1 = img1 + i

img2 = ''
with open('2.svg', 'r') as file:
    for i in file:
        img2 = img2 + i


@app.route('/', methods=['GET', 'POST'])
def index():
    global which
    if request.is_json:
        # Request is a JSON Object
        if request.method == "GET":
            # GET = send data to DOM client
            variable1 = "value_1"
            return jsonify({'svg': img1,'value1':'1'})

        if request.method == 'POST':
            # POST = receive data from DOM client
            print('POST')

            variable2 = json.loads(request.data)
            print(variable2)
            if which:
                which = not which
                return jsonify({'svg': img2, 'value1': '2'})
            else:
                which = not which
                return jsonify({'svg': img1, 'value1': '1'})

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
