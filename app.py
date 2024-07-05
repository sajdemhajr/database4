from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/articlepage')
def articlepage():
    return render_template('article-page.html')

@app.route('/article')
def article():
    return render_template('article.html')

@app.route('/imagepage')
def imagepage():
    return render_template('image-page.html')

@app.route('/image')
def images():
    return render_template('images.html')

@app.route('/user')
def user():
    return render_template('Writer-Photographer.html')

if __name__ == '__main__':
    app.run(debug=True)
    