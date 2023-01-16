import random

rasa_permen = {
    "cokelat": 16,
    "stroberi": 8,
    "vanila": 10,
    "kopi": 7,
    "mint": 12,
    "susu": 9,
    "jeruk": 5,
    "pisang": 7,
    "kayu manis": 6
}

def ambil_permen_acak(rasa_permen, jumlah_permen):
    sampel = []
    rasa_sampel = set()
    while len(rasa_sampel) < 4:
        permen = random.choice(list(rasa_permen.keys()))
        if rasa_permen[permen] > 0 and permen not in rasa_sampel:
            rasa_permen[permen] -= 1
            sampel.append(permen)
            rasa_sampel.add(permen)
    return sampel

sampel = ambil_permen_acak(rasa_permen, 4)
print("Sampel permen:", end=" ")
for i, permen in enumerate(sampel):
    if i == len(sampel) - 1:
        print(permen)
    else:
        print(permen, end=", ")

