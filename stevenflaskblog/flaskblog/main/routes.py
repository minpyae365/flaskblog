from flask import Blueprint, render_template, request
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type =int)
    #get page parameter, default is 1 and parameter type is integer to put into url
    #will throw error if not an integer is passed in.


    #posts = Post.query.all()
    #posts = Post.query.paginate(per_page = 2, page = page )
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page = 5, page = page )
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
