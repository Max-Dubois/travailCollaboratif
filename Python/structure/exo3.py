txt = str(input("Entrez un mot : "))
x = 0
voyelles = ""
for lettres in txt:
    if lettres in "aeiouyAEIOUY":
        x += 1
        voyelles += lettres + " "
print(f"Voyelles du mot : {voyelles}")