import random as rd
import datetime as dt
from customer import Customer
customer = Customer("4562224823125")

while True:

    wrongCount = 0

    while wrongCount < 3:

        inputPin = input("\nMASUKKAN PIN ATM ANDA: ")

        if customer.custPin == inputPin:
            break

        else:
            print("PIN YANG ANDA MASUKKAN SALAH")
            wrongCount += 1

    if wrongCount == 3:
        print("KARTU ATM ANDA TELAH DIBLOKIR")
        exit()

    while True:
        print("\nSELAMAT DATANG  \n1. CEK SALDO \n2. DEBET \n3. SIMPAN \n4. GANTI PIN \n5. KELUAR")
        transaction = int(input("\nSILAHKAN PILIH TRANSAKSI YANG ANDA INGINKAN: "))

        if transaction == 1:
            customer.checkBalance()

        elif transaction == 2:
            withdraw = int(input("MASUKKAN JUMLAH UANG YANG INGIN DITARIK: "))
            customer.withdrawBalance(withdraw)

        elif transaction == 3:
            deposit = int(input("MASUKKAN JUMLAH UANG YANG INGIN DISETOR: "))
            customer.depositBalance(deposit)

        elif transaction == 4:
            checkPin = input("MASUKKAN PIN YANG SEKARANG: ")
            if checkPin == customer.custPin:
                customer.custPin = input("MASUKKAN PIN YANG BARU: ")
                print("PIN ANDA BERHASIL DIUBAH")
            else:
                print("PIN YANG ANDA MASUKKAN SALAH")

        elif transaction == 5:
            print("TRANSAKSI ANDA TELAH SELESAI \nTERIMA KASIH ATAS KEPERCAYAAN ANDA")
            print("----------------------------")
            print("NO. REF : " + str(rd.randint(100000,1000000)))
            print("TANGGAL : " + dt.datetime.now().strftime("%d/%m/%y"))
            print("WAKTU   : " + dt.datetime.now().strftime("%H:%M:%S"))
            print("ID ATM  : " + customer.id)
            print("SALDO AKHIR: " + str(customer.custBalance))
            exit()

        else:
            print("PILIHAN TRANSAKSI YANG ANDA MASUKKAN SALAH")
