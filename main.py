from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        num_1 = request.form['num_1']
        num_2 = request.form['num_2']
        action = request.form['action']
        result = eval(num_1+action+ num_2)
        return render_template('index.html', status = True, result = result )

if __name__ == "__main__":
    app.run(debug=True, port=5001)

