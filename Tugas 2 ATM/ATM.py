# Nama : Abdul Quddus
# NIM  : D0220393
print("SELAMAT DATANG DI ATM")
print("PILIH OPTOIN : ")
print('1.Cek Saldo')
print('2.Penarikan')
print('3.Setor/Tabung')
option = int(input("Silahkakn pilih  option  :"))
uang_kamu=200000
if option==1:
    print('uang Anda berjumlah Rp ',uang_kamu)
elif option == 2:
    print('uang Anda berjumlah Rp 200000')
    print('1.  Rp 100.000')
    print('2.  Rp 200.000')
    print('3.  Rp 50.000')
    option2 = int(input("masukkan pilihan anda untuk penarikan : "))
    if option2 ==1:
        hasil=uang_kamu-100000
        print("uang kamu sekarang berjumlah Rp ",hasil)
    elif option2 == 2:
        hasil=uang_kamu-200000
        print("uang kamu sekarang berjumlah Rp ",hasil)
    elif option2==3:
        hasil=uang_kamu-50000
        print("uang kamu sekarang berjumlah Rp ",hasil)
    else :
        print("pilihan anda tidak terdapat dalam option")
elif option == 3:
    print("Uang Anda berjumlah Rp.200000 , mau tabung lagi ")
    option3= int(input("masukkan  jumlah uang : "))
    hasil=uang_kamu+option3
    print("jumlah uang sekarang Rp ",hasil)
else:
    print("piliihan anda salah, silahkan ulang lagi")
    
        
       
        
    
    
    