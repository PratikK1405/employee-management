from flask import Flask, request, redirect, url_for, render_template
import mysql.connector

app = Flask(__name__)

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="14052005",
        database="details"
    )

def setup_database():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            position VARCHAR(255) NOT NULL,
            salary DECIMAL(10, 2) NOT NULL,
            email_id VARCHAR(50)  NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    cursor.close()
    
def create_employee(name, position, salary, email_id):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO employees (name, position, salary, email_id) VALUES (%s, %s, %s,%s)"
    values = (name, position, salary,email_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def read_employees():
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM employees"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_employee(emp_id, name=None, position=None, salary=None,email_id=None):
    conn = connect()
    cursor = conn.cursor()
    updates = []
    values = []

    if name:
        updates.append("name = %s")
        values.append(name)
    if position:
        updates.append("position = %s")
        values.append(position)
    if salary:
        updates.append("salary = %s")
        values.append(salary)
    if email_id:
        updates.append("email_id = %s")
        values.append(email_id)

    values.append(emp_id)
    query = f"UPDATE employees SET {', '.join(updates)} WHERE id = %s"
    cursor.execute(query, tuple(values))
    conn.commit()
    cursor.close()
    conn.close()

def delete_employee(emp_id):
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(query, (emp_id,))
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    employees = read_employees()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    position = request.form['position']
    salary = request.form['salary']
    email_id = request.form['email_id']
    create_employee(name, position, salary, email_id)
    return redirect(url_for('index'))

@app.route('/update/<int:emp_id>', methods=['POST'])
def update_employee_route(emp_id):
    name = request.form.get('name')
    position = request.form.get('position')
    salary = request.form.get('salary')
    email_id = request.form.get('email_id')
    update_employee(emp_id, name, position, salary,email_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:emp_id>', methods=['POST'])
def delete_employee_route(emp_id):
    delete_employee(emp_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    setup_database()
    app.run(debug=True)
