def reverse(txt: str) -> str:
    if len(txt) == 0:
        return txt
    return reverse(txt[1:]) + txt[0]
print(reverse("deks"))