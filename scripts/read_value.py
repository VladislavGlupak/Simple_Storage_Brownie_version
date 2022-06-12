from asyncore import read
from brownie import SimpleStorage, accounts, config, network

def read_contract():
    simple_storage = SimpleStorage[-1] # most recent deployed contract
    print(simple_storage.retrieve())

def main():
    read_contract()