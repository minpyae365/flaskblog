from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=["GET" , "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data , content = form.content.data , author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!' , 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title = 'New Post' , form = form,
                            legend = 'New Post')

@posts.route("/post/<int:post_id>") #making user input in website a variable, int is specifying it's an integer
def post(post_id):
    post = Post.query.get_or_404(post_id) #get the id, if no exists return 404
    return render_template('post.html' , title = post.title , post = post )

@posts.route("/post/<int:post_id>/update", methods=["GET" , "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403) #403 is http response for forbidden route
    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()

        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))

    elif request.method == 'GET':
        form.title.data = post.title#populating
        form.content.data = post.content#populating

    return render_template('create_post.html', title = 'Update Post' , form = form,
                            legend = 'Update Post')

@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403) #403 is http response for forbidden route
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!","success")
    return redirect(url_for("main.home"))
