import sqlite3


def delete_records_by_ids(db_path, table_name, ids_to_delete):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    placeholders = ', '.join('?' for _ in ids_to_delete)

    sql_query = f"DELETE FROM {table_name} WHERE id IN ({placeholders})"

    try:
        cursor.execute(sql_query, ids_to_delete)
        conn.commit()

        print(f"Removed {cursor.rowcount} records from {table_name}.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


db_path = 'user_data.db'
table_name = 'users'
ids_to_delete = [4, 5, 6]

delete_records_by_ids(db_path, table_name, ids_to_delete)
