from flask import Flask, render_template, request

app = Flask(__name__)

#프로젝트 데이터를 저장하는 목록(데모용)
projects = []

@app.route('/')
def index():
    return render_template('produce.html')

@app.route('/create_project', methods=['POST'])
def create_project():
    project_name = request.form['project_name']
    project_code = request.form['project_code']
    project_date = request.form['project_date']
    item = request.form['item']

    # 프로젝트 데이터 저장(실제 애플리케이션에서 데이터베이스로 대체 가능)
    project_data = {
        'project_name': project_name,
        'project_code': project_code,
        'project_date': project_date,
        'item': item,
    }

    projects.append(project_data)

    # 프로젝트 생성 후 감사 페이지나 다른 적절한 페이지로 리디렉션할 수 있습니다.
    return "Project created successfully! Thank you."

if __name__ == '__main__':
    app.run(debug=True)
