# coding=utf-8

from read_config import ConfigLoader
from apis.server import app

if __name__=='__main__':
    config = ConfigLoader()
    app.run(port=int(config.get('apis', 'port')), debug=True)