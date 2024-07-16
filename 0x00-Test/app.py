import sqlite3

# Function to generate INSERT statements
def generate_inserts():
    employees = [
        ('Anthony', 30, 'Statistician'),
        ('Harrison', 22, 'Data Analyst'),
        ('Johnson', 25, 'Data Engineering')
        # Add more data as needed
    ]
    
    sql_statements = []
    for employee in employees:
        sql = f"INSERT INTO employees (name, age, department) VALUES ('{employee[0]}', {employee[1]}, '{employee[2]}');"
        sql_statements.append(sql)
    
    return sql_statements

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Generate INSERT statements
insert_statements = generate_inserts()

# Write SQL statements to file.sql
with open('table-constraint.sql', 'w') as sql_file:
    for statement in insert_statements:
        sql_file.write(statement + '\n')

# Close the connection
conn.close()