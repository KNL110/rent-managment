from tkinter import messagebox
import mysql.connector

db_connection = mysql.connector.connect(
    host="rent@localhost",
    user="knl",
    password="12345678",
    database="rent"
)
# Create a cursor object to interact with the database
cursor = db_connection.cursor()

# Create the Rent table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Rent (
        Id INT PRIMARY KEY,
        Email_Id VARCHAR(225),
        USERNAME VARCHAR(225),
        PASSWORD VARCHAR(225),
        tenant_name VARCHAR(255),
        room_No VARCHAR(255),
        amount DECIMAL(10, 2),
        due_date DATE
    )
""")
db_connection.commit()


def create_rent(Id, Email_Id, USERNAME, PASSWORD, tenant_name, room_No, amount, due_date):
    insert_query = ("INSERT INTO Rent (Id, Email_Id, USERNAME, PASSWORD, tenant_name, room_No, amount, due_date) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    data = (Id, Email_Id, USERNAME, PASSWORD, tenant_name, room_No, amount, due_date)
    cursor.execute(insert_query, data)
    db_connection.commit()


def update_rent(rent_id, new_data):
    update_query = ("UPDATE Rent SET Email_Id = %s, USERNAME = %s, PASSWORD = %s, tenant_name = %s, room_No = %s, "
                    "amount = %s, due_date = %s WHERE id = %s")
    data = (new_data['Email_Id'], new_data['USERNAME'], new_data['PASSWORD'], new_data['tenant_name'],
            new_data['room_No'], new_data['amount'], new_data['due_date'], rent_id)
    cursor.execute(update_query, data)
    db_connection.commit()


def delete_rent(rent_id):
    delete_query = "DELETE FROM Rent WHERE id = %s"
    data = (rent_id,)
    cursor.execute(delete_query, data)
    db_connection.commit()


def close_connection():
    cursor.close()
    db_connection.close()


def export_to_text(labels, data, file_path):
    with open(file_path, 'w') as file:
        file.write(f"{data[4]}'s Rent Detail""\n")
        i = 0
        while i < len(labels):
            file.write(f"{labels[i]} : {data[i]}" "\n")
            i = i + 1
        messagebox.showinfo("Success!", f"file saved to\n {file_path}")
