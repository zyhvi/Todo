import tornado.options
from tornado.options import define,options
import torndb


define('port', default = 8888, help='port', type = int)
define('mysql_host', default='127.0.0.1:3306', help='host')
define('mysql_database', default='todo', help='mysql_database')
define('mysql_user', default='root', help='user')
define('mysql_password', default='aaaaaa', help='password')

db = torndb.Connection(
	host=options.mysql_host,
	database=options.mysql_database,
	user=options.mysql_user,
	password=options.mysql_password)
