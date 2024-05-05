from django.shortcuts import render
from requests import Response
from web3 import Web3
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.views import APIView

from rest_framework import generics, renderers,viewsets
from .serializer import *
from solcx import compile_standard, install_solc
import json
from web3 import Web3

my_contract_address = "0x9F4EaC45A101Ce746F0C70f3a7448a7916d553b2"

genche_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(genche_url))
# 

my_contract_address = "0x9F4EaC45A101Ce746F0C70f3a7448a7916d553b2"
# contract = web3.eth.contract(address=my_contract_address, abi=contract_abi)

# web3.eth.default_account = web3.eth.accounts[0]



# web3.eth.default_account = web3.eth.accounts[0]

# CrowdFunding = web3.eth.contract(abi=abi, bytecode=bytecode)
# tx_hash = CrowdFunding.constructor(100, 3600).transact()  
# tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# contract_address = tx_receipt.contractAddress

# crowdfunding_contract = web3.eth.contract(address=contract_address, abi=abi)

# contract_balance = crowdfunding_contract.functions.getContractBalance().call()
# print("Contract Balance:", contract_balance)

# DEPLOY CONTRACT

def home(request):
    return render(request, "home.html")



class DeployContractManager(APIView):
    def get(self, request):
        install_solc('0.8.0')

        with open("myapp/mycontract.sol", "r") as file:
            solidity_file = file.read()

        compile_sol = compile_standard(
            {
                "language": "Solidity",
                "sources": {"mycontract.sol": {"content": solidity_file}},
                "settings": {
                    "outputSelection": {
                        "*": {
                            "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                        }
                    }
                },
            },
            solc_version="0.8.0",
        )

        with open("compiledjson.json", "w") as file:
            json.dump(compile_sol, file)

        # bytecode = compile_sol["contracts"]["mycontract.sol"]["CrowdFunding"]["evm"]["bytecode"]["object"]
        # abi = compile_sol["contracts"]["mycontract.sol"]["CrowdFunding"]["abi"]

        response_data = {"message": "Smart contract compiled successfully."}
        return JsonResponse(response_data)
    
    
    
def save_locked_tokens(request):
    if request.method == 'POST':
        token_address = request.POST.get('tokenAddress')
        amount = request.POST.get('amount')
        

        if token_address and amount:
            locked_tokens = LockedTokenModel.objects.create(
                token_address=token_address,
                amount=amount,
                target_address=my_contract_address
            )
            locked_tokens.save()
            try:
                # my_contract.functions.lockTokens(token_address, amount, releaseTime, my_contract_address).transact({'from': web3.eth.default_account})
                return JsonResponse({'status': 'success'})
            except :
                return JsonResponse({'status': 'error', 'message': str(e)})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid data provided'})

    return JsonResponse({'status': 'error', 'message': 'Method not allowed'})





