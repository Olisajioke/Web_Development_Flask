from flask import Flask
from random import randint



def makebold(func):
    def wrapper_function():
        return f"<b>{func()}</b>"
    return wrapper_function


def make_underlined(func):
    def wrapper_function():
        return f"<ul>{func()}</ul>"
    return wrapper_function

def make_emphasis(func):
    def wrapper_function():
        return f"<em>{func()}</em>"
    return wrapper_function




app = Flask(__name__)

@app.route("/")
@makebold
@make_emphasis
def index():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='GIF of a person guessing' width=500px>"



def generate_number():
    return randint(0, 9) # Generates a random number between 0 and 9

random_num = generate_number()
print(random_num)

@app.route('/guess/<int:digit>')
def guess_number(digit, random_num=random_num):
    if digit == random_num:
        return "<h1 style='text-align: center'>You found me!</h1>"\
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='GIF of a person unboxing a happy puppy' width=500px>"
                
    elif digit < random_num:
        return "<h1 style='text-align: center'>Too low, try again!</h1>"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='GIF of a dog looking down at something' width=500px>"
                
    elif digit > random_num:
        return "<h1 style='text-align: center'>Too high, try again!</h1>"\
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='GIF of a dog looking up at something' width=500px>"
    



if __name__ == "__main__":
    app.run(debug=True)