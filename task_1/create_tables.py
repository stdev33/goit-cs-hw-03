import psycopg2

connection = psycopg2.connect(
    dbname="postgres", user="postgres", password="12345678", host="localhost"
)
cursor = connection.cursor()

# Створення таблиці users
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
""")

# Створення таблиці status
cursor.execute("""
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
""")

# Створення таблиці tasks
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER REFERENCES status(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
""")

connection.commit()
cursor.close()
connection.close()
print("Таблиці створено успішно.")
