from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 샘플 사용자 데이터(실제 애플리케이션에서 데이터베이스로 대체)

users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return 'Login Successful!'
    else:
        return 'Login Failed. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)
