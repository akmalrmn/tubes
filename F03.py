def summonjin():
    if username == "Bondowoso":
        print('''Jenis jin yang dapat dipanggil:
        (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
        (2) Pembangun - Bertugas membangun candi
        ''')
    
    bool_nomor_jin = True
    while bool_nomor_jin:
        nomor_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        if nomor_jin not in ['1', '2']:
            print(f"Tidak ada jenis jin bernomor “{nomor_jin}”!")
        elif nomor_jin == '1':
            bool_nomor_jin = False
            print('Memilih jin “Pengumpul”.')
            bool_username_jin = True
            while bool_username_jin:
                username_jin = input('Masukkan username jin: ')
                if username_jin == True: #buat cara mengetahui apakah username_jin sudah ada di matriks
                    for baris in f:
                        if baris[0] == username_jin:
                            #bila username_jin sudah ada maka
                            print(f'Username {username_jin} sudah diambil!')
                else: #jika username_jin belum ada maka buat password
                    # buat loop sampai password memiliki len 5-25
                    bool_username_jin = False
                    bool_password = True
                    while bool_password:
                        password_jin = input('Masukkan password jin: ')
                        if len(password_jin) > 4 and len(password_jin) < 26:
                            print(f'''Mengumpulkan sesajen...
                            Menyerahkan sesajen...
                            Membacakan mantra...
                            Jin {username_jin} berhasil dipanggil!''')
                            bool_password = False
                        else: #jika panjang password tidak 5 sampai 25 karakter
                            print('Password panjangnya harus 5-25 karakter!')
        else: # untuk nomor jin == 2
            bool_nomor_jin = False
            print('Memilih jin “Pembangun”.')
            bool_username_jin = True
            while bool_username_jin:
                username_jin = input('Masukkan username jin: ')
                if username_jin == True: #buat cara mengetahui apakah username_jin sudah ada di matriks
                    for baris in f:
                        if baris[0] == username_jin:
                            #bila username_jin sudah ada maka
                            print(f'Username {username_jin} sudah diambil!')
                else: #jika username_jin belum ada maka buat password
                    # buat loop sampai password memiliki len 5-25
                    bool_username_jin = False
                    bool_password = True
                    while bool_password:
                        password_jin = input('Masukkan password jin: ')
                        if len(password_jin) > 4 and len(password_jin) < 26:
                            print(f'''Mengumpulkan sesajen...
                            Menyerahkan sesajen...
                            Membacakan mantra...
                            Jin {username_jin} berhasil dipanggil!''')
                            bool_password = False
                        else: #jika panjang password tidak 5 sampai 25 karakter
                            print('Password panjangnya harus 5-25 karakter!')