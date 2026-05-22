class DatabaseConnection:

    _instance = None

    def __new__(cls): # new__ method untuk memastikan hanya ada satu instance yang dibuat
        if cls._instance is None:
            cls._instance = super().__new__(cls) 
            cls._instance.connection = "Database berhasil terhubung"

        return cls._instance # mengembalikan instance yang sudah dibuat sebelumnya