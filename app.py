from flask import Flask, render_template
from flask_moment import Moment


app = Flask(__name__)
moment = Moment(app)

moment.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/podcast')
def podcast():
    return render_template('podcast.html')


@app.route('/videos')
def videos():
    return render_template('videos.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__ == '__main__':
    app.run()
