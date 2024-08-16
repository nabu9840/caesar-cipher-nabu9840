letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plain_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
offset = 5
cipher_text = []
if offset == 5:
    shifted_letters = letters[abs(offset):] + letters[: abs(offset)]
for text in plain_text:
    for i in range(26):
        if text == letters[i]:
            cipher_text.append(shifted_letters[i])
for item in cipher_text:
 print(item, end='')