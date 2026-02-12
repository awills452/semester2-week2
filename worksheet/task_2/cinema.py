"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    c = conn.cursor()
    c.execute("""
        SELECT f.title, s.screen, t.price
        FROM films f
        JOIN screenings s ON f.film_id = s.film_id
        JOIN tickets t ON t.screening_id = s.screening_id
        WHERE t.customer_id = ?
        ORDER BY f.title
    """, (customer_id,))
    result = c.fetchall()
    return result



def screening_sales(conn):
    cursor = conn.cursor()   
    query = """
        SELECT 
            s.screening_id, 
            f.title, 
            COUNT(t.ticket_id) AS tickets_sold
        FROM screenings s
        JOIN films f ON s.film_id = f.film_id
        LEFT JOIN tickets t ON s.screening_id = t.screening_id
        GROUP BY s.screening_id, f.title
        ORDER BY tickets_sold DESC;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close() 
    return results


def top_customers_by_spend(conn, limit):
   
    query = """
        SELECT 
            c.customer_name,
            SUM(t.price) AS total_spent
        FROM customers c
        JOIN tickets t ON c.customer_id = t.customer_id
        GROUP BY c.customer_id, c.customer_name
        ORDER BY total_spent DESC
        LIMIT ?;
    """
    cursor = conn.execute(query, (limit,))
    results = cursor.fetchall()
    cursor.close()
    return results