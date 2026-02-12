import sqlite3

# Connect to the database
conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("=" * 60)
print("DATABASE: tickets.db")
print("=" * 60)

if not tables:
    print("No tables found in this database.")
else:
    print(f"Found {len(tables)} tables:\n")
    
    for table in tables:
        table_name = table[0]
        print("-" * 60)
        print(f"TABLE: {table_name}")
        print("-" * 60)
        
        # Get schema
        cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        schema = cursor.fetchone()
        if schema and schema[0]:
            print(f"Schema: {schema[0]}")
        
        # Get column info
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        print("\nColumns:")
        for col in columns:
            print(f"  • {col[1]} ({col[2]}){' NOT NULL' if col[3] else ''}{' PRIMARY KEY' if col[5] else ''}")
        
        # Get row count
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        count = cursor.fetchone()[0]
        print(f"\nRow count: {count}")
        
        # Show first 3 rows if any exist
        if count > 0:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 3;")
            rows = cursor.fetchall()
            print("\nFirst 3 rows:")
            for row in rows:
                print(f"  {row}")
        print()

conn.close()