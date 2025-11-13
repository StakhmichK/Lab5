text = input("Enter your text: ")
chars = list(text)
new_chars = []

for c in chars:
    if c == " ":
        new_chars.append("_")
    else:
        new_chars.append(c)
new_text = "".join(new_chars)
print(new_text)