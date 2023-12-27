from collections import namedtuple



Config = namedtuple('Config', ['ip', 'configuration', 'revision'])

class FDataBase:
    def __init__(self, db):
        self._db = db
        self._cur = db.cursor()


    def get_conf(self, version=None):
        if version:
            querry = f"SELECT ip, config, revision FROM versions WHERE revision = '{version}'"
        else:
            return None
        try:
            self._cur.execute(querry)
            res = self._cur.fetchone()
            if res: return res
        except Exception as e:
            print(f'Ошибка чтения из БД {e}')
        return None
    
    def read_conf(self, ip=None):
        if ip:  
            querry = f"SELECT ip, config, revision from versions WHERE ip LIKE '{ip}%'"
        else:
            querry = f"SELECT ip, config, revision from versions"

        try:
            self._cur.execute(querry)
            res = self._cur.fetchall()
            res = [Config(ip, config, revision) for ip, config, revision in res]
            if res: return res
        except Exception as e:
            print(f'Ошибка чтения из БД {e}')
        return []
    
