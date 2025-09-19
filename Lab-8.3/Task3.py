def is_sentence_palindrome(sentence):
    import string
    # Remove punctuation, spaces, and convert to lowercase
    cleaned = ''.join(
        c.lower() for c in sentence if c.isalnum()
    )
    return cleaned == cleaned[::-1]

