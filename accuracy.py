import pandas as pd
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_excel('Dictionary MD sample.xlsx')  # Replace with the actual file name

# Calculate Dictionary Method Accuracy
# 'label1' is the dictionary method prediction, 'label2' is the ground truth
dictionary_accuracy = accuracy_score(df['label2'], df['label1'])

# Print Dictionary Method Accuracy
print(f"Dictionary Method Accuracy: {dictionary_accuracy:.3f}")
