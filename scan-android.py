import androidhelper

def get_friend_contacts():
    droid = androidhelper.Android()

    # Memeriksa apakah izin akses kontak telah diberikan
    if not droid.checkPermission('android.permission.READ_CONTACTS').result:
        print("Izin akses ke kontak tidak diberikan.")
        return

    # Meminta izin akses ke kontak
    droid.requestPermissions(['android.permission.READ_CONTACTS'])

    # Memeriksa apakah izin telah diberikan
    if not droid.checkPermission('android.permission.READ_CONTACTS').result:
        print("Izin akses ke kontak tidak diberikan.")
        return

    # Mendapatkan daftar kontak
    contacts = droid.contactsQuery().result

    # Memindai nomor telepon dan mendapatkan kontak teman
    friend_contacts = []
    for contact in contacts:
        if 'phones' in contact:
            for phone_number in contact['phones']:
                friend_contacts.append((contact['name'], phone_number['number']))

    return friend_contacts

# Memanggil fungsi untuk mendapatkan kontak teman
friend_contacts = get_friend_contacts()

# Menampilkan kontak teman
for name, phone_number in friend_contacts:
    print("Nama:", name)
    print("Nomor Telepon:", phone_number)
    print()
