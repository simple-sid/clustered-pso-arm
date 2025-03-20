from preprocess import preprocess_data
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules
import pandas as pd

csv_file = './data/dataset.csv'
df, transactions_with_disease, binary_transactions = preprocess_data(csv_file)

binary_df = pd.DataFrame(binary_transactions, columns=df.columns[1:])

frequent_itemsets = fpgrowth(binary_df, min_support=0.01, use_colnames=True)

# Display frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)
