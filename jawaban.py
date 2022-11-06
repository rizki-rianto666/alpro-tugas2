print(20* "=", "TIPE DATA STRING", 20* "=")
print("String")
Data_string = "Halo, ini adalah string hengkel..."
print("Nilai dari Data_string =", Data_string)
print("-------------------")

print(20* "=", "TIPE DATA NUMERIK", 20* "=")

print("Integer (int)")
Data_int = 10
print("Nilai dari Data_Int =", Data_int)
print("-------------------")

print("float")
Data_float = 10.34
print("Nilai dari Data_float =", Data_float)
print("-------------------")

print("complex")
Data_complex = 2j
print("Nilai dari Data_complex =", Data_complex)
print("-------------------")

print(20* "=", "TIPE DATA BOOLEAN", 20* "=")
print("Boolean")
Data_boolean = True
print("Nilai dari Data_boolean =", Data_boolean)
print("-------------------")

print(20* "=", "TIPE DATA SEQUENCE", 20* "=")
print("list")
Data_list = ["Item1", 2, "Item lanjutan", 2.5]
print("List merupakan tipe data yang menyatakan kumpulan item-item")
print("Nilai dari Data_list =", Data_list)
print("-------------------")

print("Tuple")
Data_tuple = "Item1", 2, "Item lanjutan", 2.5
print("Tuple merupakan tipe data yang menyatakan kumpulan item-item. Hanya saja item didalam nya bersifat tetap, tdak bisa diubah")
print("Nilai dari Data_tuple =", Data_tuple )
print("-------------------")

print("Range")
Data_range = range(5)
print("""Range e merupakan tipe data yang digunakan untuk menghasilkan number (dan biasanya berhubungan juga dengan nomor Indeks) dari jangkauan tertentu
Range ini biasanya diaplikasikan pada loop""")
print("Nilai dari Data_range =", Data_range )
print("-------------------")


print(20* "=", "TIPE DATA SET", 20* "=")

print("Set")
Data_set = set("ABCDEFG")
print("""Set merupakan koleksi atau kumpulan data yang tak tersusun, dalamnya juga tidak boleh ada duplikasi
Isi dari set sendiri bisa berupa string, Integer, list, dan lainnya""")
print("Nilai dari Data_set =", Data_set)
print("-------------------")

print(20* "=", "TIPE DATA DICTIONARY", 20* "=")
print("Dictionary")
Data_dictionary = {
    "Nama"  : "Rizki",
    "NIM"   : "i.2210881"
} #Kata Kunci  : #Nilai nya 
print("""Dictionary merupakan tipe data yang digunakan untuk menyimpan suatu nilai data. Pada Dict terdapat kata kunci dan nilai dari kata kunci tsb. """)
print("Nilai dari Data_dictionary =", Data_dictionary)
print("-------------------")

print(50*"=")
print("Untuk mengecek tipe data bisa digunakan type(variabel ataupun nilai data nya secara langsung)")
print(type(Data_int))
print(type(Data_float))
print(type(Data_complex))
print(type(Data_boolean))
print(type(Data_list))
print(type(Data_tuple))
print(type(Data_range))
print(type(Data_set))
print(type(Data_dictionary))
