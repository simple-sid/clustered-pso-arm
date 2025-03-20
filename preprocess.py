import pandas as pd

def preprocess_data(csv_file):
    df = pd.read_csv(csv_file)
    
    # Convert data to transactional format
    transactions = []
    for index, row in df.iterrows():
        transaction = [col for col in df.columns[1:] if row[col] == 1]
        transactions.append(transaction)
    
    # Optionally, add disease name to each transaction for clarity
    diseases = df.iloc[:, 0].tolist()
    transactions_with_disease = list(zip(diseases, transactions))
    
    # Convert transactions to a binary format suitable for FP-Growth
    binary_transactions = []
    for transaction in transactions:
        binary_row = [1 if symptom in transaction else 0 for symptom in df.columns[1:]]
        binary_transactions.append(binary_row)
    
    return df, transactions_with_disease, binary_transactions

# Example usage
csv_file = './data/dataset.csv'
df, transactions_with_disease, binary_transactions = preprocess_data(csv_file)

# Print results
print("Original DataFrame:")
print(df.head())
print("\nTransactions with Disease:")
print(transactions_with_disease[:5])
print("\nBinary Transactions:")
print(binary_transactions[:5])
