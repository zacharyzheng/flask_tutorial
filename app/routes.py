from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'zachary'}
    posts = [
        {
            'author':{'username':'zheng'},
            'body':'this is first'
        },
        {
            'author':{'username':'zac'},
            'body':'this is second'
        }
    ]
    return render_template('index.html', title='My', user=user, posts=posts)
