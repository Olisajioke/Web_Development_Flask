from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/cv")
def cv():
    return render_template("mycv.html")


if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
def make_bold(funt):
    def wrapper_function():
        return f"<b>{funt()}</b>"
    return wrapper_function
"""
