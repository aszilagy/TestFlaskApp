from flask import Flask, render_template, request, abort
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/home', methods=['GET','POST'])
def logs():
    if request.method == 'POST':
        user = request.form['username']
        pa = request.form['password']
        if user == 'test' and pa == 'admin':
            return render_template('templateboot.html')

    return render_template('index.html', error='Wrong username/password.')

@app.route('/post', methods=['GET', 'POST'])
def apiPost():
    if request.method == 'POST':
        print(request.get_json())
        return "200"

    return abort(404)

        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
