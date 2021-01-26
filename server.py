import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

import flask

from blockchain import BlockChain

app = flask.Flask(__name__)
node_ideantifier = str(uuid4()).replace('-','')
blockchain = BlockChain()

@app.route('/mine', methods=['GET'])
def mine():
    return "This endpoint is to mine a new block"

@app.route('/transaction/new', methods=['POST'])
def new_transaction():
    return "This endpoint creates new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return flask.jsonify(response), 200

if __name__ == '__main__':
    app.run(port=5000)