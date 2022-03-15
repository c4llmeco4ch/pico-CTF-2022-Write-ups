decoded = []
with open('message.txt') as f:
    modded = [int(num) % 37 for num in f.read().split()]
for val in modded:
    if val <= 25:
        decoded.append(chr(val + 65))
    elif val <= 35:
        decoded.append(chr(val + 22))
    else:
        decoded.append('_')
print(''.join(decoded))