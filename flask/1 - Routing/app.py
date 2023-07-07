# Flask class import
from flask import Flask, url_for, request, render_template, make_response
from werkzeug.utils import secure_filename
from markupsafe import escape

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
# url_for('static', filename='style.css')

#########################################   Rendering Templates   ##################################

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello_html', name=name)

#########################################   Request Object   #######################################

def valid_login(username, password):
    return True

def log_the_user_in(username):
    return f'{username} is logged in successfully!'

@app.route('/login_request_test', methods=['GET', 'POST'])
def login_request_test():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

#########################################   File Upload   ##########################################

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if(request.method == 'POST'):
        file = request.files['the_file']
        file.save('/var/www/uploads/uploaded_file.txt')
        
        # If you want to know how the file was named on the client before it was uploaded to your application
        file.save(f'/var/www/uploads/{secure_filename(file.filename)}')
        
#########################################   Cookies   ##############################################

@app.route('/cookie')
def cookie():
    username = request.cookies.get('username')
    

#########################################   Response   #############################################

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp



