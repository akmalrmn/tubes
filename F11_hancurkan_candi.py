def hancurkan_candi():
    import csvtolist
    import listtocsv

    # Mengubah file candi.csv menjadi list
    arr_candi = csvtolist.csv_to_list('candi.csv',101,5)

    # Input id candi 
    id_candi = input('Masukan ID candi: ')

    # Cek apakah ada candi dengan ID tersebut dan declare atas nama valid
    valid = False
    for candi in arr_candi:
        if candi[0] == id_candi:
            valid = True
    
    # Algoritma Hancurkan_candi
    if not valid :
        print('Tidak ada candi dengan ID tersebut.')        
    else :
        pilihan = input(f'Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ')
        if pilihan == 'N' :
            print("Candi gagal dihancurkan.")
        elif pilihan == 'Y' :
            # cari baris candi dengan ID tersebut
            loop = True
            row_num = 0
            i = 0
            while loop:
                if arr_candi[i][0] != id_candi:
                    i += 1
                    row_num += 1
                else :
                    loop = False

            # Membuat array baru tanpa element yang mau dihapus
            arr_candi_baru = [[None for j in range(5)] for i in range (100)]
            baris = 0
            kolom = 0
            for i in range (101):
                kolom = 0
                for j in range (5):
                    if i != row_num :
                        arr_candi_baru[baris][j] = arr_candi[i][j]
                        kolom += 1
                if i != row_num :
                    baris += 1
                    
            
            print("Candi berhasil dihancurkan")

            # Mengubah list menjadi file candi.csv
            listtocsv.list_to_csv(arr_candi_baru,'candi.csv')
