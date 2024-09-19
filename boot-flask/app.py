from flask import Flask, render_template, request, url_for, redirect
#import secrets
from flask_wtf import CSRFProtect
from forms import MyForm
#import bcrypt
from flask_bootstrap import Bootstrap


def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  app.config['SECRET_KEY'] = "olisa007"
  CSRFProtect(app)

  return app


app = create_app()



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def test():
   return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)