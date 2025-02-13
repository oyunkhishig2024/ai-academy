from flask import Flask, request, render_template
from even_odd import is_even_or_odd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_even_odd():
    number = int(request.form['number'])
    result = is_even_or_odd(number)
    return render_template('result.html', number=number, result=result)

if __name__ == '__main__':
    app.run()
