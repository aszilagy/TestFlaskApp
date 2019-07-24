from flask import Flask, render_template, request, abort, redirect, url_for
app = Flask(__name__)

#FIXME: Move this to mongodb or similar DB
userDict = {'test':'admin'}

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('index.html')

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print("Request form:",request.form)
        #if 'username' not in request.form or 'password' not in request.form:
        #    return render_template('index.html')

        user = request.form['username']
        pa = request.form['password']
        if user in userDict:
            if userDict[user] == pa:
                print("Logging into test account")
                return render_template('templateboot.html')

    return render_template('index.html', error='Wrong username/password.')

@app.route('/createAccount', methods=['POST'])
def createAccount():
    print("Hitting accountCreate")
    if request.method == 'POST':
        user = request.form['newUsername']
        pa = request.form['newPassword']
        email = request.form['newEmail']

        if user not in userDict:
            userDict[user] = pa
            print("Creating user: %s %s %s" % (user, pa, email))

        else:
            print("User already exists")

        #return redirect(url_for('home'))
        return "abc"
    

@app.route('/registration', methods=['GET'])
def register():
    return render_template('registration.html')

@app.route('/post', methods=['GET', 'POST'])
def apiPost():
    if request.method == 'POST':
        print(request.get_json())
        return "200"

    return abort(404)

        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
