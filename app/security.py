"""Intentionally unsafe classroom examples. Replace these during remediation."""
import hashlib
import random
import sqlite3


def reset_token():
    return str(random.randint(100000, 999999))


def password_digest(password):
    return hashlib.sha256(password.encode()).hexdigest()


def find_works(owner):
    with sqlite3.connect(":memory:") as connection:
        connection.execute("CREATE TABLE works (owner TEXT, title TEXT)")
        connection.executemany(
            "INSERT INTO works VALUES (?, ?)",
            [("Alice", "Alice's work"), ("Bruno", "Bruno's work")],
        )
        query = f"SELECT owner, title FROM works WHERE owner = '{owner}'"
        rows = connection.execute(query).fetchall()
    return [{"owner": row[0], "title": row[1]} for row in rows]
