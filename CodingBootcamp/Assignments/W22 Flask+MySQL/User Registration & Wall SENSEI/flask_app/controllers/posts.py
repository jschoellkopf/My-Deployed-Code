from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.post import Post


@app.route('/create_post', methods=["POST"])
def createPost():
    if not Post.validate_post(request.form):
        return redirect('/wall')
    
    data = {
        "content": request.form['post_content'],
        "user_id": session['user_id']
    }
    Post.save(data)
    return redirect('/wall')


@app.route('/delete_post/<int:id>')
def deletePost(id):
    Post.delete(id)
    return redirect('/wall')

