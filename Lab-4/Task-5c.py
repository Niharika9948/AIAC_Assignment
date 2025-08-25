import string

def analyze_word_frequency(paragraph):
    # Convert to lowercase
    text = paragraph.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    # Count word frequency
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Few-shot prompting examples
examples = [
    {
        "input": "My name is Niha.",
        "output": analyze_word_frequency("My name is Niha.")
    },
    {
        "input": "I’m from Kataram.",
        "output": analyze_word_frequency("I’m from Kataram.")
    },
    {
        "input": "I completed my schooling in Montessori.",
        "output": analyze_word_frequency("I completed my schooling in Montessori.")
    }
]

# Show the few-shot examples
for i, ex in enumerate(examples, 1):
    print(f"Example {i}:")
    print(f"Input: {ex['input']}")
    print(f"Output: {ex['output']}")
    print()

# Accept user input and analyze
user_para = input("Enter a paragraph: ")
result = analyze_word_frequency(user_para)
print("Word frequency:", result)
