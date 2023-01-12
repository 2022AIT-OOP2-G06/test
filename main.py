from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def display_IMG():
    result = "konntya"
    return render_template("play.html")

@app.route("/action", methods=['POST'])
def action():
    print("ppp")
    if request.method == 'POST':
        # if request.form['send'] == 'skill1':
        #     m = '12345'
        if request.form['send'] == 'skill1':
            m = '12345'

        elif request.form['send'] == 'skill2':
                m = '12345'

        elif request.form['send'] == 'skill3':
                m = '12345'

        elif request.form['send'] == 'skill4':
                m = '12345'

        return render_template('play.html', res=m)



if __name__=='__main__':
    app.run(debug=True)