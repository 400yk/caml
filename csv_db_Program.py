from ca.models import Program
import MySQLdb
import csv

db = MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd = "root",
        db = "test_caml"
        )

cur = db.cursor()
# Change encoding of all tables to utf8_general_ci
cur.execute('SHOW TABLES')
results=[]
for row in cur.fetchall(): results.append(row)
for row in results: cur.execute('ALTER TABLE %s CONVERT TO CHARACTER SET utf8 COLLATE     utf8_general_ci;' % (row[0]))
# Change the database charset
cur.execute("ALTER DATABASE test_caml CHARACTER SET utf8;")

query = "INSERT INTO ca_program VALUES ("
args = ""
with open('Program Profile-Table 2.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
    next(spamreader, None)
    for row in spamreader:
        for index, eachValue in enumerate(row):
            if index < 34:
                # Check if eachValue is an integer
                try:
                    dummy = float(eachValue)
                    query += eachValue
                except ValueError:
                    query += '"'
                    query += eachValue
                    query += '"'
                query += ','
                #args += eachValue
        query = query[0:len(query)-1]
        query += ');'
        print (query)
        print len(query)
        query = "INSERT INTO ca_program VALUES ("
        #args = tuple(args)
        #print args
        #print len(args)
        #cur.execute(query, row)
        cur.execute(query)

db.commit()
