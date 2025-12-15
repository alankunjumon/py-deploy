import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# --- 1. CONNECT TO THE DATABASE ---
# Improvement: Add a fallback to SQLite for local testing safety
db_url = os.environ.get("DB_URL", "sqlite:///local.db")

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- 2. DEFINE THE MODEL ---
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id}: {self.text}>'

# --- 3. ROUTES ---
@app.route('/')
def index():
    tasks = Todo.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task_text')
    if task_text:
        new_task = Todo(text=task_text)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

# --- 4. AUTO-CREATE TABLES & RUN ---
if __name__ == '__main__':
    # This block runs only when you execute 'python app.py'
    # It creates tables automatically before the server starts listening
    with app.app_context():
        db.create_all()
        print("Connected to DB and tables created!")
        
    app.run(host='0.0.0.0', port=5000)