import argparse
import asyncio
import aiohttp
from aiohttp import web
from demo import create_app
from demo.settings import load_config
# uvloop альтернатива базовому eventloop он работает быстрее

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print('Library uvloop is not avaible')

#конфигурация проекта с командной строки
parser = argparse.ArgumentParser(description='Demo_Project')
parser.add_argument('--host', help='Host to listen', default='0.0.0.0')
parser.add_argument('--port', help='Port to accept connections', default=5000)
#чтобы проект можно было запускать в режиме разработчика при перезапуске проекта aioreloader
parser.add_argument('--reload', action='store_true', help='Autoreload code on change')

parser.add_argument('-c', '--config', type=argparse.FileType('r'),
                     help='Path to configuration file')

args = parser.parse_args()

app = create_app(config=load_config(args.config))

if args.reload:
    print('Start with code reload')

if __name__ == '__main__':
    web.run_app(app, host=args.host, port=args.port)