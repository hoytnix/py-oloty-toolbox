from random import choice # returns a random member of an array


# Cache dictionary.
dictionary = []
with open('dict.txt', 'r') as stream:
    for line in stream:
        dictionary.append(line.strip())

def dictionary_word():
   return choice(dictionary) 

# Map-structure.
char_map = {
    'a': ['@'],
    'i': ['1', '!'],
    's': ['$'],
    'o': ['0']
}

def main():
    words = []
    word_length = 4
    for word in range(word_length):
        words.append(dictionary_word())
    
    plain_pwd = '-'.join(words)
    hard_pwd = ''
    for char in plain_pwd:
        if char in char_map:
            hard_pwd += choice(char_map[char])
        else:
            hard_pwd += char

    print(hard_pwd)

if __name__ == '__main__':
    main()
