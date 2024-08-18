from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        name = request.form['name']
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.execute(f"SELECT * FROM member WHERE name = '{name}'")
                results = cursor.fetchall()
                conn.close()
            except sqlite3.Error as e:
                print(f"SQL query failed: {e}")
    # GET 요청이거나, POST 요청 후에도 페이지를 렌더링합니다.
    return render_template_string('''
        <h1>Member Search</h1>
        <form method="post" action="/">
            <p>Enter member name:</p>
            <input type="text" name="name">
            <input type="submit" value="Search">
        </form>
        {% if results %}
            <h2>Member Information:</h2>
            <ul>
                {% for row in results %}
                    <li>No: {{ row['no'] }}, ID: {{ row['user_id'] }}, Name: {{ row['name'] }}, Email: {{ row['email'] }}, Date: {{ row['date'] }}</li>
                {% endfor %}
            </ul>
        {% elif request.method == 'POST' %}
            <p>No member found with that name.</p>
        {% endif %}
    ''', results=results)

if __name__ == '__main__':
    app.run(debug=True)
