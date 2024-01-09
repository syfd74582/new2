from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # تحقق هنا من اسم المستخدم وكلمة المرور
    if username == 'admin' and password == 'password':
        # إذا تحققت المعلومات، قم بتوجيه المستخدم إلى المجلد
        return redirect(url_for('open_folder'))

    # إذا لم تتطابق المعلومات، عادة ما يتم إعادة تحميل صفحة تسجيل الدخول مع رسالة خطأ
    return render_template('login.html', error='Invalid username or password')

@app.route('/open_folder')
def open_folder():
    folder_path = r"C:\Users\LENOVO\Desktop\template"
    os.startfile(folder_path)
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)