from flask import Flask, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home', methods=['GET','POST'])
def logs():
    if request.method == 'POST':
        user = request.form['username']
        pa = request.form['password']
        if user == 'test' and pa == 'admin':
            return "Logging"

    return render_template('index.html', error='Wrong username/password.')
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
