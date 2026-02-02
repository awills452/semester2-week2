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
    

    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    pass


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    pass