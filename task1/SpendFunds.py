# Spend Locked Fund
from bitcoin import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

# Private key and Bitcoin address from the previous step
private_key = CBitcoinSecret.from_secret_bytes(...)
address = P2PKHBitcoinAddress.from_pubkey(...)

# Create a transaction input (UTXO)
txid = ’...’

# Transaction ID of the UTXO you want to spend
output_index = ...

# Index of the output in the transaction
txin = create_txin(txid, output_index)

# Create a transaction output to the desired destination
destination_address = ’...’

# Recipient’s address
amount_to_send = ...

# Amount to send in satoshis
txout = create_txout(amount_to_send, destination_address)

# Create the transaction
tx = create_signed_transaction([txin], [txout], [private_key])

# Broadcast the transaction
broadcast_tx(tx)