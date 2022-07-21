import MySQLdb
import MySQLdb.cursors
import timeit
start = timeit.default_timer()
connection = MySQLdb.connect(
        host="localhost", user="root", passwd="passwordroot69", db='app', 
        cursorclass=MySQLdb.cursors.SSCursor) # put the cursorclass here
cursor = connection.cursor()
cursor.execute('SELECT * FROM user;')
print(cursor)
for row in cursor:
    print(row)
stop = timeit.default_timer()
print('Time: ', stop - start) 