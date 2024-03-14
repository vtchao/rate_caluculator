from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_interest', methods=['POST'])
def calculate_interest():
    principal = float(request.form['principal'])
    rate = float(request.form['rate'])
    days = int(request.form['days'])

    interest = principal * (days / 365) * (rate / 100)
    return jsonify({'interest': interest})

@app.route('/calculate_rate', methods=['POST'])
def calculate_rate():
    principal = float(request.form['principal'])
    interest = float(request.form['interest'])
    days = int(request.form['days'])

    rate = (interest / principal) * (365 / days) * 100
    return jsonify({'rate': rate})

if __name__ == '__main__':
    app.run(debug=True)
