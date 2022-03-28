"""
FINDING THE KEY
"""
from typing import TextIO  # Specific annotations

def shift(text: str, n: int) -> str:
    """
    Shift n times to the right using ord and chr (Unicode)
    1 - with boundaries from a-z
    2 - spaces stay the same
    3 - punctuation and symbol stay the same
    4 - given the shift step n to jump
    """
    result = ''
    for char in text:
        distance = ord(char) - ord('a')
        distance += n
        if distance >= 26:
            distance -= 26
        if ord(char) >= 97 and ord(char) <= 122:
            new_char = chr(ord('a') + distance)
            result += new_char
        else:
            result += char
    return result
            

def decrypt(input_file: TextIO, wordlist_filename: str) -> str:
    """
    Using wordlist_filename, decrypt input_file according to the handout
    instructions, and return the plaintext.
    """
    encrypt = []
    result = ''
    ans = ''
    plaintext = ''

    # store English wordlist into a set
    english_wordlist = set()
    with open(wordlist_filename) as file:
        for line_text in file:
            english_wordlist.add(line_text.strip())
    
    for line in input_file:
        encrypt = line.lower()
    
        max_so_far = 0
        for count in range(26):
            text = shift(encrypt, count).split()
            #print(text)
            # reset max end every new shift
            max_end = 0
            # check if English word match the text
            # add 1 whenever there is a match
            for word in text:
                # remove symbol & punctuation
                words = ''.join(char for char in word if char.isalnum())
                if words in english_wordlist:
                    max_end += 1
            # if new max found, set the result to that text
            # and set max_so_far to new max
            #print(max_end)
            if max_so_far < max_end:
                result = ' '.join(text)
                max_so_far = max_end
        ans += result + '\n'
    return ans.strip()

if __name__ == "__main__":
    print(decrypt(open('book2.txt'), 'wordlist.txt'))

