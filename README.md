
🔥 **BlackOut - DDoS Attack Simulator**

 📌 Overview
BlackOut is a powerful tool designed to simulate Distributed Denial of Service (DDoS) attacks for **educational** and **ethical** purposes. It provides a controlled environment to stress-test servers and networks with customizable attack modes. 

With support for **TCP** and **UDP** attack types, this tool lets you simulate realistic attack scenarios. Key features include the ability to use **random IP addresses** in the packet header, **multiple targets** per attack, and **customizable thread count**.

---

 ⚙️ **Key Features**
- ✅ **TCP + UDP Flood per Target**: Choose between TCP and UDP attack modes to simulate different types of DDoS attacks.
- ✅ **Attack Multiple Targets**: Launch attacks on multiple targets at the same time.
- ✅ **Random IP Addresses (Spoofed IPs)**: Every packet uses a random source IP address to simulate real-world DDoS scenarios.
- ✅ **Threads per Target**: Customize the number of threads for each target to control the attack's intensity.
- ✅ **Dark Grey + Red GUI**: Sleek, dark-themed interface with red accents for a dramatic look.
- ✅ **Live Attack Counter**: Displays real-time stats of packets sent and packets per second.
- ✅ **Attack Duration Timer**: Automatically stops the attack after the specified duration.
- ✅ **Visualization**: Live updates of packets sent, packets per second, and target status.
- ✅ **EXE Version**: Available as an executable for easy use.

---

🖥️ **User Interface Layout**
```
------------------------------------------------------
| [ Target IPs     ] [ Port ] [ Attack Type TCP/UDP ] |
| [ Threads ] [ Attack Duration (sec) ]              |
|                                                    |
| [ Start Attack 🔥 ] [ Stop Attack 🛑 ]              |
|                                                    |
| Packets Sent: 3453 Packets/sec: 570                |
| Progress Bar showing load... ▓▓▓▓▓▓░░░░░░ 55%      |
|                                                    |
| (Black background, Red buttons, White text)        |
------------------------------------------------------
```

---

📝 **How to Use**

1. **Run the Script as Admin/Root**: For raw socket functionality, run the script as an administrator (on Windows) or with root privileges (on Linux/macOS).
   
2. **Open the GUI**: The GUI will open once the script is executed.

3. **Enter the Following Information**:
   - **Target IPs**: Separate multiple IPs with commas (e.g., `192.168.1.1,192.168.1.2`).
   - **Target Port**: Enter the port number of the target.
   - **Attack Type**: Choose between TCP or UDP.
   - **Threads per Target**: Specify how many threads you want to use for each target.

4. **Start the Attack**:
   - Click **"🔥 Start Attack"** to begin sending packets.
   
---

🔧 **How the Attack Works**
- **Random Source IP Address**: Each packet will have a random source IP address.
- **Random Source Port**: Each packet will have a random source port.
- **TCP Attack**: Fake SYN packets are sent to the target, simulating a TCP flood.
- **UDP Attack**: Junk UDP payloads are sent to the target.
  
The tool will run until you either stop the attack manually or let the timer automatically stop after the specified duration.

---

💡 **Technical Details**
- **GUI Framework**: Tkinter
- **Packet Crafting**: Uses `socket` and `struct` libraries to craft raw packets.
- **OS Support**: Compatible with Windows, Linux, and macOS. **Requires admin/root privileges** for raw socket access.

---

 🖤 **Design and Color Scheme**
- **Background**: Dark grey (#121212)
- **Text/Buttons**: Red (#FF0000) for a striking contrast
- **Font Color**: White for readability

---

⚠️ **Important Notes**
- **Run as Administrator/Root**: This tool requires elevated privileges to send raw packets. Ensure you have the necessary permissions.
- **Ethical Use**: Use this tool responsibly for educational and ethical purposes only. Unauthorized DDoS attacks are illegal and unethical.



