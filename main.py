def encrypt(p_text, key):
    e_text = [''] * key
    current_position = 0
    direction = 1

    for char in p_text:
        e_text[current_position] += char
        current_position += direction

        if current_position == 0 or current_position == key - 1:
            direction = -direction
    # for i in e_text:
    #     for j in i:
    #         print (j,"\t", end="")
    #     print()
    return ''.join(e_text)

def decrypt(c_text, key):
    d_text = [''] * len(c_text)
    current_position = 0
    direction = 1

    for i in range(len(c_text)):
        d_text[i] = c_text[i]
        current_position += direction

        if current_position == 0 or current_position == key - 1:
            direction = -direction
    return ''.join(p_text)

p_text = "TAHMID HASAN"
key = 3
print("Plain Text:", p_text)
print("Key:", key)

e_text = encrypt(p_text, key)
print("Encrypted Text:", e_text)

d_text = decrypt(e_text, key)
print("Decrypted Text:", d_text)
