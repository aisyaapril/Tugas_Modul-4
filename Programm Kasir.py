#TIPE DATA STRING & INTEGER
menu = {
    "1. Moachi Isi Kacang tanah \t" : 27000,
    "2. Moachi Isi Green tea \t" : 35000,
    "3. Moachi Isi Coklat \t\t" : 30000,
    "4. Moachi Isi Nanas \t\t" : 35000
}

#PERULANGAN FOR
print("========= Aneka Macam Moachi =========")
print("Daftar Moachi \t\t\t Harga")
for i in menu :
    print(i , menu[i])
print("======================================")
beli = input("Silahkan pilih list moachi yang mau dibeli : ")
jumlah = int(input("Jumlah moachi : "))

#PENGKONDISIAN IF...ELSEIF...ELSE    
if beli == str(1):
    macam = "Moachi Isi Kacang tanah"
    harga = 27000
    bayar = jumlah * harga
elif beli== str(2):
    macam = "Moachi Isi Green tea"
    harga = 35000
    bayar = jumlah * harga
elif beli == str(3):
    macam = "Moachi Isi Coklat"
    harga = 30000
    bayar = jumlah * harga
elif beli == str(4):
    macam = "Moachi Isi Nanas"
    harga = 35000 
    bayar = jumlah * harga
else :
    print("Moachi tersebut tidak tersedia")

print("\n")

#FUNCTION/METHOD 
def Struk_Pembayaran (macam, harga, jumlah, bayar):
    print("****** TOKO MOACHI GEMINI ******")
    print(" Agen Moachi Gemini 'Kentangan'")
    print("  Jalan Baterman Besar No. 300")
    print("******** SELAMAT DATANG ******** \n") 
    print(macam, "\n" , harga, "×", jumlah, "\t\t" , bayar)
    print("--------------------------------")
    print("Total", "(",(jumlah),")", "\t\t", bayar)
    print("")
    uang = int(input("Bayar \t\t\t "))
    kembalian = uang - bayar
    print("Kembalian \t\t", kembalian)
    print("")
    print("********* TERIMA KASIH *********")
Struk_Pembayaran(macam, harga, jumlah, bayar)