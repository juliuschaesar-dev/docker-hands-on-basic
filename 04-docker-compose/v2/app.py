import os

import redis
import psycopg2
from flask import Flask

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:password@db:5432/mydb')
REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')


@app.route('/')
def hello_world():
    return 'Hello from Flask + Postgres + Redis! Try /db or /redis.'


@app.route('/db')
def check_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute('SELECT version();')
        version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return f'Connected to Postgres! {version}'
    except Exception as exc:
        return f'Failed to connect to Postgres: {exc}', 500


@app.route('/redis')
def check_redis():
    try:
        r = redis.Redis.from_url(REDIS_URL)
        count = r.incr('hits')
        return f'Connected to Redis! This page has been hit {count} times.'
    except Exception as exc:
        return f'Failed to connect to Redis: {exc}', 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
