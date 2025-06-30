import sqlite3

class CommentData():
    def __init__(self, number, comment, star):
        self.number = number
        self.comment = comment
        self.star = star

    def __str__(self):
        return "{}. Yorum: {}\nYıldız: {}\n".format(self.number, self.comment, self.star)

class SetData():
    def __init__(self):
        self.create_connection()

    #TABLO YOKSA OTOMATIK OLUŞTURUR
    def create_connection(self):
        self.connection = sqlite3.connect("comments.db")
        self.cursor = self.connection.cursor()

        query = '''
                CREATE TABLE IF NOT EXISTS comments (
                    number INTEGER PRIMARY KEY AUTOINCREMENT,
                    comment TEXT NOT NULL,
                    star INTEGER NOT NULL
                )'''
        self.cursor.execute(query)
        self.connection.commit()
        print("bağlantı kuruldu")

    def add_comment(self, comment, star):
         query = "INSERT INTO comments (comment, star) VALUES (?, ?)"
         self.cursor.execute(query, (comment, star))
         self.connection.commit()

    def delete_comment(self, number):
        query = "DELETE FROM comments WHERE number = ?"
        self.cursor.execute(query, (number,))
        self.connection.commit()
        print("Yorum Başarıyla Silindi...")


    def show_all(self):
        query = "SELECT * FROM comments"
        self.cursor.execute(query)
        comments = self.cursor.fetchall()

        if len(comments) == 0:
            print("Toplamda {} Yorum Bulunuyor... ".format(len(comments)))
        else:
            for i in comments:
                print("-------------------------")
                comment = CommentData(i[0], i[1], i[2])
                print(comment)
                print("-------------------------")

            
    def disconnect(self):
        self.connection.close()
