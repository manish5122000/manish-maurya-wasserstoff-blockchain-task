from solcx import compile_standard, install_solc
import json
from web3 import Web3

# Install Solidity compiler version 0.8.0 if not already installed
install_solc('0.8.0')

# Load Solidity code from a file
with open("./solidity.sol", "r") as file:
    solidity_file = file.read()
    # print(solidity_file)

# Compile the Solidity code using Solidity compiler version 0.8.0
compile_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"solidity.sol": {"content": solidity_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",  # Set the Solidity compiler version to 0.8.0
)

# print(compile_sol)

# with open("compiled_json.json", "w") as file:
#     json.dump(compile_sol, file)

# bytecode = compile_sol["contracts"]["solidity.sol"]["CrowdFunding"]["evm"]["bytecode"]["object"]
# # print(bytecode)
# # get abi

# abi = compile_sol["contracts"]["solidity.sol"]["CrowdFunding"]["abi"]
# # print(abi)

# genche_url = 'http://127.0.0.1:7545'
# web3 = Web3(Web3.HTTPProvider(genche_url))

# web3.eth.default_account = web3.eth.accounts[0]

# CrowdFunding = web3.eth.contract(abi=abi, bytecode=bytecode)
# tx_hash = CrowdFunding.constructor(100, 3600).transact()  # Example constructor parameters: target=100, deadline=1 hour
# tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# contract_address = tx_receipt.contractAddress

# crowdfunding_contract = web3.eth.contract(address=contract_address, abi=abi)

# contract_balance = crowdfunding_contract.functions.getContractBalance().call()
# print("Contract Balance:", contract_balance)




# genche_url = 'http://127.0.0.1:7545'
# web3 = Web3(Web3.HTTPProvider(genche_url))


# account1 = "0xB61d3A1B86d15A6709E3C92927C7EaDa837057dc"
# account2 = "0x4b5b05895a8BE310b1497eF4a42396d25ECCCef2"


# private_key = "0x8a36fe5dedaaf4a6becc36fea1846b6849815b9e610579fbeabd90b62853a013"  # Replace with your actual private key

# nonce = web3.eth.get_transaction_count(account1)

# txn = {
#     'nonce': nonce,
#     'to': account1,
#     'value': web3.to_wei(1, 'ether'),  
#     'gas': 2000000,  
#     'gasPrice': web3.to_wei(50, 'gwei'), 
# }

# signed_txn = web3.eth.account.sign_transaction(txn, private_key)

# txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
# txn_hashing_valu = web3.to_hex(txn_hash)
# print("hash value",txn_hashing_valu)
# txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hashing_valu)

# # txn_hashing_valu = web3.to_hex(txn_hash)

# get_contract = web3.eth.contract(address=txn_receipt.contractAddress, abi=abi)

# print(get_contract.functions.getContractBalance().call())


