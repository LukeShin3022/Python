from flask import Flask, render_template
from datetime import datetime
import random as rand


app = Flask(__name__)

@app.route('/')
def home():
    rand_num = rand.randint(1,100)
    cur_year = datetime.today().year
    return render_template("index.html", num = rand_num, year = cur_year)

if __name__ == "__main__":
    app.run(debug=True)