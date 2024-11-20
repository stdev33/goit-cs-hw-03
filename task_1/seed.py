import psycopg2
from faker import Faker

fake = Faker()

connection = psycopg2.connect(
    dbname="postgres", user="postgres", password="12345678", host="localhost"
)
cursor = connection.cursor()

# Заповнення таблиці status
statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cursor.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;", (status,))

# Заповнення таблиці users
for _ in range(10):
    cursor.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING;",
        (fake.name(), fake.email())
    )

# Заповнення таблиці tasks
for _ in range(20):
    cursor.execute(
        """
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES (%s, %s, %s, %s);
        """,
        (
            fake.sentence(nb_words=6),
            fake.text(),
            fake.random_int(min=1, max=len(statuses)),
            fake.random_int(min=1, max=10)
        )
    )

connection.commit()
cursor.close()
connection.close()
print("Таблиці заповнено даними.")