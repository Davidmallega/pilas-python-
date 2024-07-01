from flask import Flask, render_template
from controllers import admin_bp, user_bp

app = Flask(__name__)

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)







