# Mengambil input dari pengguna
input_string = input("Masukkan string: ")

# Mencari posisi huruf "@" dalam string
at_position = input_string.find("@")

# Membuat list teks yang akan ditambahkan setelah huruf "@"
text_list = [f"{i}" for i in range(1, 1001)]

# Menambahkan teks setelah huruf "@" dan menyimpan hasilnya dalam file worldlist
with open("worldlist.txt", "w") as f:
    for text in text_list:
        new_string = input_string[:at_position+1] + text
        f.write(new_string + "\n")

# Menampilkan pesan sukses
print("Worldlist telah disimpan dalam file worldlist.txt")
