import os
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import GoogleSearchForm
from GoogleNews import GoogleNews

app = Flask(__name__)
SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY



@app.route("/")
@app.route("/home")
def home():
    form = GoogleSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('news'))
    return render_template('home.html', title='Google Search', form=form)


@app.route("/news",methods=['GET', 'POST'])
def news():
    period  =  str(request.form['period'])
    keyword = str(request.form['keyword'])
    googlenews = GoogleNews(period = period)
    googlenews.search(keyword)
    result = googlenews.result()
    return render_template('news.html', result = result)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

if __name__ == '__main__':
    app.run()