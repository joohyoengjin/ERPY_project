from flask import Flask, render_template

app = Flask(__name__)

# 게시판 게시물의 더미 데이터(시연용)

posts = [
    {'title': 'Post 1', 'content': 'This is the content of post 1.'},
    {'title': 'Post 2', 'content': 'This is the content of post 2.'},
    {'title': 'Post 3', 'content': 'This is the content of post 3.'},
]

@app.route('/')
def bulletin_board():
    return render_template('bulletin_board.html', posts=posts)

@app.route('/create')
def create_post():
    # 실제 애플리케이션에서는 이 경로에 새 게시물 생성
    return "Create a new post here."

if __name__ == '__main__':
    app.run(debug=True)
