from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
from dotenv import load_dotenv



load_dotenv()
app = Flask(__name__,static_url_path='/static/style.css')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


####################################################
### DataBase Setup #########
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# postgresql://pranav:KjiYDkfns7p93MpOQt73KcsrqvHhtOgR@dpg-chn7l4fdvk4n43adgchg-a.oregon-postgres.render.com/blog_website_36if


db = SQLAlchemy(app)
Migrate(app,db)

#################



#####################################################
login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"



#####################################################

from company_blog.core.views import core
from company_blog.users.views import users
from company_blog.blog_posts.views import blog_posts
from company_blog.error_pages.handlers import error_pages

# Register the apps
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(core)
app.register_blueprint(error_pages)