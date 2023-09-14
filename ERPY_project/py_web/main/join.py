from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 등록된 사용자를 저장할 목록 (실제 애플리케이션에서 데이터베이스로 대체)
registered_users = []

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    employee_number = request.form['employee_number']
    position = request.form['position']
    department = request.form['department']
    contact_address = request.form['contact_address']
    contact = request.form['contact']

    # 사용자 데이터 저장(데이터베이스 저장소로 대체 ​​가능)
    user_data = {
        'name': name,
        'employee_number': employee_number,
        'position': position,
        'department': department,
        'contact_address': contact_address,
        'contact': contact,  
    }

    registered_users.append(user_data)

    # 등록 후 감사 페이지나 기타 적절한 페이지로 
    # 리디렉션(URL 리디렉션은 한 URL에서 다른 URL로 사용자를 보내는 웹 서버의 기능)할 수 있습니다.
    return "Registration successful! Thank you for signing up."

if __name__ == '__main__':
    app.run(debug=True)
