import re
import csv
import pandas as pd

# Function to detect toxicity
def detect_toxicity(comment, toxic_words):
    words = re.findall(r'\b\w+\b', comment.lower())  # Tokenize words in the comment
    toxic_count = sum(1 for word in words if word in toxic_words)
    return toxic_count > 0  # Return True if toxic word is found

# Load the comments from the text file
with open('comments.txt', 'r', encoding='utf-8', errors='ignore') as file:
    comments = [line.strip() for line in file.readlines()]

# Load the toxic words list from the text file
with open('toxic_words.txt', 'r', encoding='utf-8', errors='ignore') as file:
    toxic_words = [line.strip() for line in file.readlines()]

# Prepare a list of results (comment, toxic/non-toxic)
results = []

# Detect toxic comments and label them
for comment in comments:
    if detect_toxicity(comment, toxic_words):
        results.append({'comment': comment, 'label': 'toxic'})
    else:
        results.append({'comment': comment, 'label': 'non-toxic'})

# Save the results to a CSV file
with open('comment_toxicity_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['comment', 'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print(f"Toxicity results saved to 'comment_toxicity_results.csv'")

# Load the CSV file
df = pd.read_csv('comment_toxicity_results.csv') 

# Calculate the total number of comments
total_comments = len(df)

# Calculate the number of toxic and non-toxic comments
toxic_count = len(df[df['label'] == 'toxic'])
non_toxic_count = len(df[df['label'] == 'non-toxic'])

# Calculate the percentages
toxic_percentage = (toxic_count / total_comments) * 100
non_toxic_percentage = (non_toxic_count / total_comments) * 100

# Print the results
print(f"Percentage of toxic comments: {toxic_percentage:.2f}%")
print(f"Percentage of non-toxic comments: {non_toxic_percentage:.2f}%")