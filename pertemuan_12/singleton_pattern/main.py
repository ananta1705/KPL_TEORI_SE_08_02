from src.database_connection import DatabaseConnection

def main():
    db1 = DatabaseConnection()

    print(db1.connection) # Output: Database berhasil terhubung

if __name__ == "__main__":
    main()