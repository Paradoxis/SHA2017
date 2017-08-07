def reverse_nibbles(data):
    return bytes(bytearray.fromhex(' '.join(hex(b)[2:].zfill(2)[::-1] for b in data[::-1])))


with open("reverse", "rb") as input_, open("reverse.png", "wb") as output:
    output.write(reverse_nibbles(input_.read()))

