def kali(start_num, last_num, pattern): #start_num adalah angka pertama, last_num adalah angka terakhir dalam kasus pertambahan, sedangkan pattern adalah pola perubahan angka(7 jika mengacu pola soal)
    while start_num != last_num:
        start_num = start_num * pattern
    return start_num

print(len(str(kali(4,132931722278404, 7))))