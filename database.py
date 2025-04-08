import sqlite3

def get_all_payments(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Payment")

    data = cursor.fetchall()

    return data

def get_payment_by_id(conn, payment_id):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Payment WHERE id = ?", (payment_id,))

    data = cursor.fetchone()

    return data

def update_payment_by_id(conn,id, user_id, plan_id, method_id):

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE payment 
    SET user_id = ?, 
        plan_id = ?, 
        method_id = ?
    WHERE id = ?;
    """, (user_id, plan_id, method_id, id))

    conn.commit()

    return True

def create_payment(conn, user_id, plan_id, method_id):

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO payment (
        user_id, 
        plan_id, 
        method_id           
    ) VALUES (?, ?, ?);
    """, (user_id, plan_id, method_id))

    conn.commit()

    return cursor.lastrowid

def get_all_plans(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Plan")

    data = cursor.fetchall()

    return data

def get_plan_by_id(conn, plan_id):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Plan WHERE id = ?", (plan_id,))

    data = cursor.fetchone()

    return data

def get_all_methods(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Method")

    data = cursor.fetchall()

    return data

def get_method_by_id(conn, method_id):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Method WHERE id = ?", (method_id,))

    data = cursor.fetchone()

    return data

def update_student_id_by_financial_id(conn, student_id, financial_id):

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE payment 
        SET user_id = ? 
        WHERE id = ?;
    """, (student_id,financial_id))

    conn.commit()
    
    return True

def delete_payment_by_id(conn, payment_id):

    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM payment
        WHERE id = ?;
    """, (payment_id,))
    
    conn.commit()

    return True