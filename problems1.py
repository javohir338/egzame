def harf(matn):
    unlilar = "aeiou"
    unli = 0
    undosh = 0
    for i in matn.lower():
        if not i.isalpha():
            continue
        if i in unlilar:
            unli += 1
        else:
            undosh += 1
    return {"unli": unli, "undosh": undosh}