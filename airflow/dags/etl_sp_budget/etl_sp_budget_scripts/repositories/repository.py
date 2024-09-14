class Repository():
    def __init__(self, connection):
        self.connection = connection

    def update(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()