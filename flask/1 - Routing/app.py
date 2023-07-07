# Flask class import
from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

###################################################################################################
#########################################    Example   ############################################
###################################################################################################

# Create a instance of Flask class. The first argument is the name of the application's module or package.
# @__name__ argument is convenient shortcut. This is needed to look for resources as templates or static files.
app = Flask(__name__)

# Use route() decorator to tell Flask what URL should trigger the function.
@app.route('/')
def index():
    return 'Index Page'

@app.route('/string')
def string():
    return 'Hello, world'

@app.route('/html')
def html():
    return '<p>Hello, world</p>'

###################################################################################################
#########################################    Routing   ############################################
###################################################################################################

#########################################   Variable Rules   ######################################

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"


#########################################   Unique URLs /Redirection Behavior   ###################

# If user access /projects, it will be redirect to /projects/
@app.route('/projects/')
def projects():
    return "The project page"

# If user access /about/, it will produce 'Not Found' 404 error.
@app.route('/about')
def about():
    return "The about page"


#########################################   URL Building   ########################################

@app.route('/index')
def index2():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f"{username}'s profile"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


#########################################   HTTP Methods   ########################################
def do_the_login():
    return 'Logged in'

def show_the_login_form():
    return 'Try again'

@app.route('/http_login', methods=['GET', 'POST'])
def http_login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
#########################################   Static Files   #########################################
url_for('static', filename='style.css')