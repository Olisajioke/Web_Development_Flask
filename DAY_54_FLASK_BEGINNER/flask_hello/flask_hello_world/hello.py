from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper_function():
        return f"<b>{func()}</b>"
    return wrapper_function

    
def make_emphasis(func):
    def wrapper_function():
        return f"<em>{func()}</em>"
    return wrapper_function
    
    
def make_underlined(func):
    def wrapper_function():
        return f"<u>{func()}</u>"
    return wrapper_function


@app.route('/')
def hello_world():
    return 'Hello, World! Welcome to my webpage!'


@app.route('/mercy')
@make_bold
@make_emphasis
@make_underlined
def justmercy():
    return "<h1 style='text-align: center'> HELLO DOCTOR FRANKLIN</h1>"\
              "<h2 style='text-align: left'> Let's make this money!!</h2>"\
                  '<img src="https://th.bing.com/th/id/OIP.K3UHyw69sNOqFWhEb0AAJwHaEm?w=290&h=180&c=7&r=0&o=5&pid=1.7" alt="Image of Benedict Cumberbatch as Doctor Strange casting spells" width=900px>'


@app.route("/username/<anything>")
def greet_user(anything):
    return f"Hello, {anything}, Nice to have you here!"




@app.route("/user/<username>/<int:age>")
def add_users(username, age):
    return "<h1 style='background; linear-gradient(red, green)'>Hello, {username}, {age} years old, you have been added to the database!</h1>"



if __name__ == "__main__":
    app.run(debug=True)