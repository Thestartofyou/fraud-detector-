import pandas as pd

# Load the transaction data into a DataFrame
transaction_data = pd.read_csv('transaction_data.csv')

# Define a function to identify suspicious transactions
def detect_fraud(transaction):
    if transaction['amount'] > 1000:
        return 'High amount transaction'
    
    if transaction['merchant'] == 'Unusual Merchant':
        return 'Unusual merchant transaction'
    
    if transaction['country'] != 'USA':
        return 'Foreign transaction'
    
    # Add more conditions as needed based on your fraud detection rules
    
    return 'No fraud detected'

# Apply the fraud detection function to each transaction
transaction_data['fraud_status'] = transaction_data.apply(detect_fraud, axis=1)

# Filter and display suspicious transactions
suspicious_transactions = transaction_data[transaction_data['fraud_status'] != 'No fraud detected']
print(suspicious_transactions)
