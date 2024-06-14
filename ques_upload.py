
import csv
import sqlite3

db=sqlite3.connect("student.db")
db.execute('''CREATE TABLE IF NOT EXISTS test_table
                    (Q_number INT NOT NULL,
                    Question TEXT NOT NULL,
                    Option_A TEXT NOT NULL,
                    Option_B TEXT NOT NULL,
                    Option_C TEXT NOT NULL,
                    Option_D TEXT NOT NULL,
                    Answer TEXT NOT NULL   
                    )''')


# print(dir(csv))
with open('ques.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        db.execute(f'''INSERT INTO test_table 
                (Q_number, Question, Option_A, Option_B, Option_C, Option_D, Answer)
                VALUES {tuple(row)};''')
        db.commit()