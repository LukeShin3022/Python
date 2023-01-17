from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style = "text-align: center">Hello World!</h1>'\
        '<p>This is a paragraph.</p>' \
        '<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width=200>'

@app.route("/bye")
def say_bye():
    return 'Bye'

@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"<h1>Hello there {name}, you are {number} years old!"

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
    # app.run(debug=True)dd
# hello_world()