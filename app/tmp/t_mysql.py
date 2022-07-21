from MySQLdb import _mysql
import timeit
start = timeit.default_timer()
db=_mysql.connect("localhost","arwell","password","app")
db.query('SELECT * FROM user;')
r=db.store_result()
r.fetch_row()
stop = timeit.default_timer()
print('Time: ', stop - start) 