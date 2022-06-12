from turtle import up
from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    # account = get_account[0]
    # account = accounts.load("testing")
    #account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account})
    #print(account)
    #print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)

    update_tx = simple_storage.store(15, {"from": account})
    update_tx.wait(1) # wait 1 block

    updated_value = simple_storage.retrieve()
    print(updated_value)
    
def get_account():
    if (network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()