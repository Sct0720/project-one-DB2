import os
import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
        )
        return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

st.title("Create Supplier")
st.subheader("Add New Suppliers")
supplier_name = st.text_input("supplier Name")
supplier_email = st.text_input("Supplier email")
supplier_phone = st.text_input("Supplier phone number")

if st.button("Add Supplier"):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO suppliers (name, email, phone)
                VALUES (%s, %s)
            """
            cursor.execute(query, supplier_name, supplier_email, supplier_phone )
            connection.commit()
            st.success("Supplier added successfully")
        except Error as e:
            st.error(f"Error adding supplier: {e}")
        finally:
            cursor.close()
            connection.close()

st.subheader("Suppliers Table")
connection = connect_to_db()
if connection:
    try:
        df = pd.read_sql("SELECT name AS Name, email AS Emails, phone AS Phone_Number  FROM suppliers", connection)
        st.dataframe(df)
    except Error as e:
        st.error(f"Error fetching data: {e}")
    finally:
        connection.close()