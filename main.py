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
    if request.method == "POST":
        #POST
        if 'jinja2' in request.form:
            if which:
                img = img1
                which = not which
                return render_template('index.html',svg_placeholder=img)

            else:
                img = img2
                which = not which
                return render_template('index.html',svg_placeholder=img)

    if request.method == "GET":
        #GET
        if which:
            img = img1
        else:
            img = img2
        return render_template('index.html',svg_placeholder=img)


@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == "POST":
        ajax_data = request.get_json()
        print(ajax_data['ajax'])

    results = {'processed': 'true'}
    return jsonify(results)


if __name__ == '__main__':
        app.run(debug=True)
