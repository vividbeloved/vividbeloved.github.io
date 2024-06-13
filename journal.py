class Journal:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_entries(self):
        return self.entries

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for entry in self.entries:
                file.write(entry + '\n')


def main():
    my_journal = Journal()

    while True:
        print("\n=== Jurnal Saya ===")
        print("1. Tambah Entri")
        print("2. Tampilkan Entri")
        print("3. Simpan dan Keluar")

        choice = input("Pilih tindakan: ")

        if choice == '1':
            entry = input("Masukkan entri baru: ")
            my_journal.add_entry(entry)
            print("Entri berhasil ditambahkan!")
        elif choice == '2':
            print("\n=== Semua Entri ===")
            entries = my_journal.get_entries()
            if entries:
                for idx, entry in enumerate(entries, 1):
                    print(f"{idx}. {entry}")
            else:
                print("Belum ada entri.")
        elif choice == '3':
            filename = input("Masukkan nama file untuk menyimpan jurnal: ")
            my_journal.save_to_file(filename)
            print(f"Jurnal berhasil disimpan dalam file '{filename}'.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
