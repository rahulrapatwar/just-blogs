from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'ABC XYZ',
        'title': 'Bolg Post 1',
        'content': 'First post content',
        'date_posted': 'May 01, 2020',
    },
    {
        'author': 'New Author',
        'title': 'Bolg Post 2',
        'content': 'Second post content',
        'date_posted': 'May 01, 2020',
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)