import string
from collections import Counter

def most_frequent_word(paragraph):
    
    # Convert to lowercase
    paragraph = paragraph.lower()
    # Remove punctuation
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = paragraph.split()
    # Count word frequency
    freq = Counter(words)
    # Find the most frequent word
    most_common = freq.most_common(1)
    return most_common[0][0] if most_common else None

# Few-shot prompting examples
# Example 1
para1 = "My name is,Anumala Niharika"
print(most_frequent_word(para1))  # Output: 'my' or 'name' or 'is' or 'anumala' or 'niharika' (all appear once)

# Example 2
para2 = "I'm from kataram"
print(most_frequent_word(para2))  # Output: 'im' or 'from' or 'kataram' (all appear once)

# Example 3
para3 = "I completed my schooling at Montessori"
print(most_frequent_word(para3))  # Output: 'i' or 'completed' or 'my' or 'schooling' or 'at' or 'montessori' (all appear once)

# Example 4
para4 = "Python is great. Python is easy to learn. Python is popular."
print(most_frequent_word(para4))  # Output: 'python' (appears 3 times)