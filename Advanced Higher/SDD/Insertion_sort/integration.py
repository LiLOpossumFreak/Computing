#connect to database please ?
import mysql.connector  # type: ignore[import-not-found]

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='sloco')
c = con.cursor()

c.execute("""SELECT * FROM athletics""")

for row in c:
  print('pupilName', row[0])
  print('yearGroup', row[1])
  print('event', row[2])
  print('eventTime', row[3])
c.close()