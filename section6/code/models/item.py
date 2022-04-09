import sqlite3

class ItemModel:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT *  from items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {"item": {"name": row[0], "price": row[1]}}
        return {"message": "Item not found"}, 404

        
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (item["name"], item["price"]))

        connection.commit()
        connection.close()
    
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "UPDATE  items SET price=? WHERE name=?"
        cursor.execute(query, (item["name"], item["price"]))

        connection.commit()
        connection.close()