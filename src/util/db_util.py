from dataclasses import dataclass
from contextlib import contextmanager

import psycopg2


@dataclass
class DBConnection:
    db: str
    user: str
    password: str
    host: str
    port: int = 5432 # default value


class DBConnection:
    def __init__(self):

        credential = DBConnection(
            user=os.getenv('WAREHOUSE_USER', ''),
            password=os.getenv('WAREHOUSE_PASSWORD', ''),
            db=os.getenv('WAREHOUSE_DB', ''),
            host=os.getenv('WAREHOUSE_HOST', ''),
            port=int(os.getenv('WAREHOUSE_PORT', 5432)),
        )

        self.conn_url = (f'postgresql://{credential.user}:{credential.password}@'
            f'{credential.host}:{credential.port}/{credential.db}'
        )

    @contextmanager
    def cursor(self, cursor_factory=None):
        self.conn = psycopg2.connect(self.conn_url)
        self.conn.autocommit = True
        self.curr = self.conn.cursor(cursor_factory=cursor_factory)
        try:
            yield self.curr
        finally:
            self.curr.close()
            self.conn.close()