import string

def caesar(text,shift,alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:]+alphabet[:shift]
    
    shiffted_alphabet=tuple(map(shift_alphabet,alphabets))

    # print(shiffted_alphabet)

    final_alphabets=''.join(alphabets)
    # print(final_alphabets)
    final_shifted_alphabets=''.join(shiffted_alphabet)
    # print(final_shifted_alphabets)
    table=str.maketrans(final_alphabets,final_shifted_alphabets)
    print(table)

    return text.translate(table)


plain_text="This is new test.Hello World"

print(caesar(plain_text,7,[string.ascii_uppercase,string.ascii_lowercase,string.punctuation]))