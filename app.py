from flask import Flask, render_template, request, flash
from my_module import get_quotes, CATEGORIES

app = Flask(__name__)
app.secret_key = "mkhjkltiz7890"


@app.route('/')
def index():
    flash("Choose a category:")
    return render_template('index.html', categories=CATEGORIES)


@app.route('/get_quotes', methods=['POST'])
def get_quotes_for_category():
    category = request.form['category']
    quotes = get_quotes(category)
    flash("Quotes:")
    return render_template('index.html', category=CATEGORIES, quotes=quotes)


if __name__ == '__main__':
    app.run(debug=True)
