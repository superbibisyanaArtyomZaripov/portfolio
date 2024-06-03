#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    text = request.form.get('text')
    email = request.form.get('email')
    button_discord = request.form.get('button_discord')
    button_python = request.form.get('button_python')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    with open('form.txt', 'a',encoding='utf-8') as f:
        f.write(email + " " + text + " " + "\n")
    return render_template('index.html', button_python=button_python
                           ,button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db,text=text,email=email)

    


if __name__ == "__main__":
    app.run(debug=True)