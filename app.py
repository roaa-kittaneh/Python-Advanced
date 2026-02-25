from flask import Flask

app = Flask(__name__)

# Route 1
@app.route('/')
def welcome():
    return "<h1>Welcome to the Student Portal!</h1><p>This is my first Flask app.</p>"

# Route 2: Dynamic route with a variable (/hello/<name>)
@app.route('/hello/<name>')
def hello(name):
    return f"<h2>Hello, {name.capitalize()}!</h2><p>Great to see you here.</p>"

if __name__ == '__main__':
    app.run(debug=True)