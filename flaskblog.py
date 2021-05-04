from flask import Flask, render_template, url_for
app = Flask(__name__)

posts= [
    {
        'author': 'Greg Flores',
        'title': 'Blog 1',
        'content': 'Some cool content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Sam Aguilar',
        'title': 'Blog 2',
        'content': 'Some cooler content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html.j2', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html.j2', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)