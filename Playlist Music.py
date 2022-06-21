class Node:
    def __init__ (self, dataplaylist):
        self.next = None
        self.prev = None
        self.dataplaylist = dataplaylist

class DoublyLinkedlist:
    def __init__ (self):
        self.start_node = None

    def Append_List(self, dataplaylist):
        if self.start_node is None:
            newNode = Node(dataplaylist)
            newNode.prev = None
            self.start_node = newNode
            
        else:
            newNode = Node(dataplaylist)
            current = self.start_node 
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = None

    def PlaySong(self):
        if self.start_node is None:
            print("="*30)
            print("| The Playlist is None |")
            print("="*30)
            return
        else:
            current = self.start_node
            out = current.dataplaylist.split(',')

        print(f"""
                                                             
        !                                                     !
        !   Kamu sedang memutar lagu {out[0]} , dari {out[1]} !        
        !                                                     !
        """)


    def NextMusic(self):
        if self.start_node is None:
            print("="*30)
            print("| The Playlist is None |")
            print("="*30)
            return
        else:
            current = self.start_node = self.start_node.next
            out = current.dataplaylist.split(',')
        print(f"""
        
                                                              
        !                                                     !
        !   Kamu sedang memutar lagu {out[0]} , dari {out[1]} !             
        !                                                     !
        """)

    def PrevMusic(self):
        if self.start_node is None:
            print("="*30)
            print("| The Playlist is None |")
            print("="*30)
            return
        else:
            current = self.start_node = self.start_node.prev
            out = current.dataplaylist.split(',')
        print(f"""
     
                                                              
        !                                                      !
        !   Kamu sedang memutar lagu {out[0]} , dari {out[1]}  !     
        !                                                      !
        """)
    
    def Delete(self):
        if self.start_node is None:
            print("Tidak ada playlist untuk dihapus")
            return
        if self.start_node is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None 


    def Show(self):
        if self.start_node is None:
            print("="*30)
            print("| The Playlist is None |")
            print("="*30)
            return
            
        else:
            no = 0
            current = self.start_node
            print("~ Playlist Anda ~")
            print("="*30)
            while current is not None:
                no +=1
                print(f"{no}.", current.dataplaylist)
                current = current.next
            print("="*30)

show = DoublyLinkedlist()
while True:

    menu = int(input("""
    _______________________________________

    |   🎼🎼🎶PLAYLIST MUSIC PLAYER SPODIFYY🎼🎶🎼   |
    |   1. Buat playlist kamu                           |
    |   2. Putar lagu                                   |
    |   3. Putar selanjutnya                            |
    |   4. Putar sebelumnya                             |
    |   5. Lihat playlist kamu                          |
    |   6. Hapus Playlist                               |
    _______________________________________
    0. Keluar.
    Pilih menu : """))
    if menu == 1:
        jumlah = int(input("Masukan jumlah lagu dalam playlist : "))
        for i in range(jumlah):
            input_lagu = input(f"Masukkan lagu ke-{i+1} (judul, singer) : ")
            show.Append_List(input_lagu)

        else:
            print("="*35)
            print("| Playlist Berhasil di Tambahkan. |")
            print("="*35)
    elif menu == 2:
        show.PlaySong()
    elif menu == 3:
        show.NextMusic()
    elif menu == 4:
        show.PrevMusic()
    elif menu == 5:
        show.Show()
    elif menu== 6:
        show.Delete()
    elif menu == 0:
        print("🎼🎶TERIMAKASIH TELAH MENGGUNAKAN SPODIFYY🎼🎶")
        exit()