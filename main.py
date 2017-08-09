from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return 'This is the Home PAge'

@app.route("/profile/<name>")
@app.route("/profile")
def profile(name=None):
    return  render_template("profile.html", name=name)

@app.route('/post/<int:post_id>')
def post(post_id):
    return  'Post id is %s' % post_id

@app.route('/method')
def method():
    return 'Method used is %s' % request.method



@app.route('/changemethod', methods=['GET', 'POST'])
def changemethod():
    if request.method == 'POST':
        return "You ara Using POST"
    else:
        return "you are using GET"


@app.route('/shop')
def shop():
    food = ["chesse", "meat","burger"]
    return  render_template("shopping.html", food=food)


if __name__ == "__main__":
    app.run(debug=True)