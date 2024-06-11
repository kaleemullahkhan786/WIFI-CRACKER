---

### WIFI-CRACKER

WIFI-CRACKER is a tool designed to simplify the use of Hashcat for cracking WPA/WPA2 handshakes. This tool automates the process of converting .cap files to Hashcat-compatible formats and running Hashcat with the specified wordlist.

#### Features

- Converts .cap files to .hc22000 format using hcxpcapngtool
- Runs Hashcat with the specified wordlist
- Provides a user-friendly interface for cracking WPA/WPA2 handshakes

#### Prerequisites

- Hashcat
- hcxpcapngtool
- colorama (for terminal colors)

#### Installation

Before using WIFI-CRACKER, make sure to install the necessary packages:

```sh
sudo apt update
sudo apt install -y hashcat hcxtools
pip install colorama
```

#### Usage

1. Run the script:

```sh
python wificracker.py
```

2. Follow the on-screen instructions to select an option and provide the necessary file paths.

#### Author

Kaleemullah Khan

---

#### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

#### Copyright

© 2024 Kaleemullah Khan

---
