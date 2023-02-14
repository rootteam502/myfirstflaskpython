from flask import Flask, render_template, request

app = Flask(__name__)

questions = []
"""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_question', methods=['GET','POST'])
def submit_question():
    if request.method == "POST":
        question = request.form.get('question')
        questions.append(question)
    return render_template('index.html', questions=questions)
"""
@app.route('/', methods=['GET','POST'])
def submit_question():
    if request.method == "POST":
        question = request.form.get('question')
        questions.append(question)
        return render_template('index.html', questions=questions)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
