import re

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

# Detect toxic comments
toxic_comments = [comment for comment in comments if detect_toxicity(comment, toxic_words)]

# Save the toxic comments to a new text file
with open('toxic_comments.txt', 'w', encoding='utf-8', errors='ignore') as file:
    for comment in toxic_comments:
        file.write(comment + '\n')

print(f"{len(toxic_comments)} toxic comments saved to 'toxic_comments.txt'")
