from web3 import Web3

# Connect to the Ethereum network (local, testnet, or mainnet)
web3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/51b164f73a8b419f8620f9b0bbaad085'))


contract_address = '0xE82F7f2687E1609da8F7e329fF94831766c1d224'


contract_abi = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "string",
                "name": "message",
                "type": "string"
            }
        ],
        "name": "Log",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "get",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "x",
                "type": "uint256"
            }
        ],
        "name": "set",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]


contract = web3.eth.contract(address=contract_address, abi=contract_abi)


def get_contract_value():
    try:

        value = contract.functions.getValue().call()


        if value is None or value == 0:
            raise ValueError("No valid number returned from the contract.")

        print(f"Value from contract: {value}")
        return value
    except Exception as e:
        print(f"Error: {e}")

        while True:
            try:
                user_value = int(input("Please enter a valid value: "))
                print(f"User entered value: {user_value}")
                return user_value
            except ValueError:
                print("Invalid input. Please enter a numeric value.")



get_contract_value()