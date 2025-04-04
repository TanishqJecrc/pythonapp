from flask import Flask, render_template

from datetime import datetime
app = Flask(__name__)

@app.route('/hello/', methods=['GET'])
def create():
    return render_template('index.html', message="Hello, World!")

@app.route('/datetime/', methods=['GET'])
def get_datetime():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', message=f"Current Date and Time: {current_time}")

if __name__ == '__main__':
    app.run(debug=True)
