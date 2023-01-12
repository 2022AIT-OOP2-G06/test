from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/select", methods=['GET'])
def display_IMG():
    ids = os.listdir('static/IMG')
    
    paths = ['IMG/' + i for i in ids]
    ids = [i.replace('.png', '') for i in ids]
    
    return render_template("select.html", ids=ids, paths=paths)

@app.route("/play", methods=["POST"])
def submit():
    data = request.get_json()
    use = data['use']
    print(use)
    return jsonify({'use': use})


@app.route("/action", methods=['GET', 'POST'])
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