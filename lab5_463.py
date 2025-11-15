text = input("Enter your text: ")
new_chars = []
in_space = False
for c in text:
    if c == " ":
        if not in_space:
            new_chars.append("_")
            in_space = True
    else:
        new_chars.append(c)
        in_space = False
new_text = "".join(new_chars)
print(new_text)