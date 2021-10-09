import string
import random

printable_chars = string.ascii_letters + string.digits + string.punctuation
nbr_chars = int(input('How many chars: '))

for i in range(nbr_chars):
    print(random.choice(printable_chars), end='')
