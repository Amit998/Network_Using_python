import string
plain_text='Hello World'


shift=65

shift %=26

print(shift)

alphabet=string.ascii_lowercase


# print(alphabet)
shifted=alphabet[shift:]+alphabet[:shift]
# print(shifted)

table=str.maketrans(alphabet,shifted)
# print(table)

encrypted=plain_text.translate(table)
# print(encrypted)