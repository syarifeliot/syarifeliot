import platform

from scapy.all import *
import platform

def arp_scan(network):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network)
    result = srp(arp_request, timeout=2, verbose=False)[0]

    clients = []
    for sent, received in result:
        hostname = get_hostname(received.psrc)  # Mengambil nama host terkait dengan alamat IP
        device_name = get_device_name()  # Mengambil nama perangkat
        clients.append({'ip': received.psrc, 'mac': received.hwsrc, 'hostname': hostname, 'device_name': device_name})

    return clients

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = "Unknown"
    return hostname

def get_device_name():
    return platform.node()

# Contoh penggunaan:
network = "192.168.100.1/25"  # Ganti dengan jaringan yang ingin Anda scan

scan_result = arp_scan(network)
print("|-----------------------------------------|")
print("|DAFTAR NAMA PRANGKAT DI JARINGAN YG SAMA:|")
print("|-----------------------------------------|")
for client in scan_result:
    print("IP:", client['ip'])
    print("MAC:", client['mac'])
    print("Hostname:", client['hostname'])
    print("Nama Perangkat:", client['device_name'])
    print("----------------------------------------")
