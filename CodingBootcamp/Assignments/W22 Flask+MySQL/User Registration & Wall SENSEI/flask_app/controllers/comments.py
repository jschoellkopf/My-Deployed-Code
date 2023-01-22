from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.comment import Comment


@app.route('/create_comment', methods=["POST"])
def create_comment():
    if not Comment.validate_comment(request.form):
        return redirect('/wall')
    
    data = {
        "comment": request.form['comment'],
        "user_id": session['user_id'],
        "post_id" : request.form['post_id']
    }
    Comment.save(data)
    return redirect('/wall')


# @app.route('/delete_post/<int:id>')
# def deletePost(id):
#     Post.delete(id)
#     return redirect('/wall')

