#TIPE DATA STRING & INTEGER
menu = {
    "1. Moachi Isi Kacang tanah \t" : 27000,
    "2. Moachi Isi Green tea \t" : 35000,
    "3. Moachi Isi Coklat \t\t" : 32000,
    "4. Moachi Isi Stroberi \t\t" : 35000,
    "5. Moachi Isi Nanas \t\t" : 45000
}

#PERULANGAN FOR
print("========= Aneka Macam Moachi =========")
print("Daftar Moachi \t\t\t Harga")
for i in menu :
    print(i , menu[i])
print("======================================")
beli = input("Silahkan pilih list moachi yang ingin dibeli : ")
jumlah = int(input("Jumlah moachi yang ingin dibeli : "))
if jumlah < 0 :
    print("Maaf jumlah moachi tidak valid")
    exit
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
    harga = 32000
    bayar = jumlah * harga
elif beli == str(4):
    macam = "Moachi Isi Stroberi"
    harga = 35000 
    bayar = jumlah * harga
elif beli == str(5):
    macam = "Moachi Isi Nanas"
    harga = 45000
    bayar = jumlah * harga
else :
    print("Maaf, Moachi tersebut tidak tersedia")
    exit

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
