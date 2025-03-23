import sqlite3

def get_all_payments(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Payment")

    data = cursor.fetchall()

    return data

def get_payment_by_id(conn, payment_id):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Payment WHERE id = ?", (payment_id))

    data = cursor.fetchone()

    return data

def get_all_plans(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Plans")

    data = cursor.fetchall()

    return data

def get_plan_by_id(conn, plan_id):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Plans WHERE id = ?", (plan_id))

    data = cursor.fetchone()

    return data