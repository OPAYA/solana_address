"""API server that accepts requests and return values."""
import logging
import logging.config
import os
from tkinter import Image
from urllib.request import Request

from fastapi import FastAPI, Response
from pydantic import BaseModel
import pandas as pd
import json

import sys
import base64
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
os.chdir(basedir)
print(sys.path)


def get_address(category):
    
    if category == 'dex':
        data = {}
        df = pd.read_csv('data/dex.csv', index_col=0)
        for i, address in enumerate(df['address'].tolist()):
            data[i] = {'address': address}
        return data

    elif category == 'nft':
        data = {}
        df = pd.read_csv('data/nft.csv', index_col=0)
        for i, address in enumerate(df['address'].tolist()):
            data[i] = {'address': address}
        return data

    elif category == 'transfer':
        data = {}
        df = pd.read_csv('data/transfer.csv', index_col=0)
        for i, address in enumerate(df['address'].tolist()):
            data[i] = {'address': address}
        return data

    elif category == 'voting':
        data = {}
        df = pd.read_csv('data/voting.csv', index_col=0)
        for i, address in enumerate(df['address'].tolist()):
            data[i] = {'address': address}
        return data

    else:
        raise
    
app = FastAPI()

class Item(BaseModel):
    address: str

@app.get("/")
def server_check() -> bool:
    return True

@app.get("/dex")
def get_defi_address():
    result = get_address('dex')
    return result

@app.get("/nft")
def get_defi_address():
    result = get_address('nft')
    return result

@app.get("/transfer")
def get_defi_address():
    result = get_address('transfer')
    return result

@app.get("/voting")
def get_defi_address():
    result = get_address('voting')
    return result