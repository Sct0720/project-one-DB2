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

def bulk_insert(df, connection):
    cursor = connection.cursor()
    for _, row in df.iterrows():
        query = """
            INSERT INTO products (name, description, price, quantity, id_category, id_supplier) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, tuple(row))
    connection.commit()
    st.success("Data loaded successfully")

def get_categories(connection):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id_category, name FROM categories")
    categories = cursor.fetchall()
    cursor.close()
    return categories

def get_suppliers(connection):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id_supplier, name FROM suppliers")
    suppliers = cursor.fetchall()
    cursor.close()
    return suppliers

st.title("Create Product")

connection = connect_to_db()
categories = get_categories(connection) if connection else []
suppliers = get_suppliers(connection) if connection else []
if connection:
    connection.close()
    
category_names = [category['name'] for category in categories]
category_ids = {category['name']: category['id_category'] for category in categories}
supplier_names = [supplier['name'] for supplier in suppliers]
supplier_ids = {supplier['name']: supplier['id_supplier'] for supplier in suppliers}

st.subheader("Add New Product")
nombre = st.text_input("Product Name")
descripcion = st.text_area("Product Description")
precio = st.number_input("Price", min_value=0.0, format="%.2f")
cantidad = st.number_input("Quantity", min_value=0, step=1)
selected_category = st.selectbox("Select Category", category_names)
selected_supplier = st.selectbox("Select Supplier", supplier_names)

if st.button("Add Product"):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            id_categoria = category_ids[selected_category]
            id_proveedor = supplier_ids[selected_supplier]
            query = """
                INSERT INTO products (name, description, price, quantity, id_category, id_supplier)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query)
            connection.commit()
            st.success("Product added successfully")
        except Error as e:
            st.error(f"Error adding product: {e}")
        finally:
            cursor.close()
            connection.close()

st.subheader("Products Table")
connection = connect_to_db()
if connection:
    try:
        df = pd.read_sql("SELECT name, description, price, quantity FROM products", connection)
        st.dataframe(df)
    except Error as e:
        st.error(f"Error fetching data: {e}")
    finally:
        connection.close()

st.subheader("Upload Excel Files")
file1 = st.file_uploader("Upload File 1", type=['xlsx'])
file2 = st.file_uploader("Upload File 2", type=['xlsx'])

if st.button("Load"):
    if file1 is not None and file2 is not None:
        try:            
            df_file1 = pd.read_excel(file1)
            df_file2 = pd.read_excel(file2)            
            df_concatenated = pd.concat([df_file1, df_file2], ignore_index=True)            
            connection = connect_to_db()
            if connection:
                bulk_insert(df_concatenated, connection)
        except Exception as e:
            st.error(f"Error loading files: {e}")
    else:
        st.warning("Please upload both Excel files before loading.")
