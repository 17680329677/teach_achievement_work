import asyncio
import easyapi
from app.config import Config

#loop = asyncio.get_event_loop()

mysql_db = easyapi.MysqlDB(Config.MYSQL_USER, Config.MYSQL_PASSWORD, Config.MYSQL_HOST, Config.MYSQL_PORT,
                           Config.MYSQL_DATABASE)

mysql_db.connect()
#loop.run_until_complete(mysql_db.connect())