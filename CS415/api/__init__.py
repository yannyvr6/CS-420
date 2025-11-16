try:
	import pymysql
except Exception:
	class _pymysql_stub:
		@staticmethod
		def install_as_MySQLdb():
			# No-op stub when pymysql is not installed (prevents import errors in editors/environments).
			return
	pymysql = _pymysql_stub()

pymysql.install_as_MySQLdb()
