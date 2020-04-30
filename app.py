from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html')

@app.route('/overview', methods=['GET', 'POST'])
def overview():
    return render_template('overview.html')

@app.route('/featured', methods=['GET', 'POST'])
def featured():
    return render_template('featured.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/#popup-sign-up', methods=['GET', 'POST'])
def sign():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
