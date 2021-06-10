import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Cache the contract on load
@st.cache(allow_output_mutation=True)

# Define the load_contract function
def load_contract():
    # Load Education Token ABI
    with open(Path('./abi1.json')) as f:
        education_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
    print(contract_address)

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi= education_abi
    )

    # Return the contract from the function
    return contract

# Load the contract
contract = load_contract()

#Image of Edu Token
from PIL import Image
image = Image.open('edutoken1.JPG')
st.image(image,  caption='Edu Token')

# Title Of Project Token
st.title("Education Token")
st.subheader("Please submit this Token form for government financial aid funding. ")

# List of Accounts
accounts = w3.eth.accounts
account = accounts[0]

#Select student account in order to issue Token
st.subheader("Please enter your student name.")
name = st.text_input("")
st.subheader("What's your student Address ? ")
student = st.selectbox("", options=accounts)

contract.functions.student_name(student , name).transact({'from': "0x3a1f44c125680faA8c47ccf360742f8980655c03", 'gas': 1000000})

# Token rules
st.subheader("Note: Maximum number of token issued per semester is 16. 1 token for each credit. ")

# Token Transfer Transaction
st.subheader("How many tokens you need this semester ?  ")
token_transfer = st.text_input("ُEnter the number of Tokens")

if st.button("Issue Tokens"):
    token_transfer = int(token_transfer)
    contract.functions.transfer(student, token_transfer).transact({'from': account, 'gas': 1000000})

# Get the balance of Tokens after Transfer
st.subheader("Please hit the display button to see total tokens issued to your student account. ")
if st.button("Display Balance Tokens"):
    balance = contract.functions.balances(student).call()
    st.write(f"The number of tokens left in balance {balance}")


# Get the Main balance of Tokens after Transfer
st.subheader("Please hit display button to see token in Main account. ")
if st.button("Display Main Balance Tokens"):
    main_balance = contract.functions.main_balances().call()
    st.write(f"The number of tokens left in financial aid account {main_balance}")

hat = Image.open('hat.JPG')
st.image(hat,  caption='Token')







