# The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z
decoded = []
mod = 41
with open('message.txt') as f:
    modded = [int(num) % mod for num in f.read().split()]
for val in modded:
    # https://www.delftstack.com/howto/python/mod-inverse-python/
    inv = pow(val, -1, mod)
    if inv <= 26:
        decoded.append(chr(inv + 64))
    elif inv <= 36:
        decoded.append(chr(inv + 21))
    else:
        decoded.append('_')
print(''.join(decoded))