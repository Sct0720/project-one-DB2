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

st.title("Create Category")
st.subheader("Add New Category")
category_name = st.text_input("Category Name")
category_description = st.text_area("Category Description")

if st.button("Add Category"):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO categories (name, description)
                VALUES (%s, %s)
            """
            cursor.execute(query, (category_name, category_description))
            connection.commit()
            st.success("Category added successfully")
        except Error as e:
            st.error(f"Error adding category: {e}")
        finally:
            cursor.close()
            connection.close()

st.subheader("Categories Table")
connection = connect_to_db()
if connection:
    try:
        df = pd.read_sql("SELECT name, description FROM categories", connection)
        st.dataframe(df)
    except Error as e:
        st.error(f"Error fetching data: {e}")
    finally:
        connection.close()
