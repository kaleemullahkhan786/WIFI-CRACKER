# This script is intended for educational purposes only. It should be used responsibly and ethically.
# This tool simplifies the usage of Hashcat, a password recovery tool. Hashcat is commonly used for security testing and forensic purposes.
import os
import subprocess
import time
from colorama import Fore, Style, init

init(autoreset=True)

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    # Display a colorful and animated banner with the tool name
    banner_lines = [
        " __       __  ______  ________  ______         ______                                __                           ",
        "/  |  _  /  |/      |/        |/      |       /      \\                              /  |                          ",
        "$$ | / \\ $$ |$$$$$$/ $$$$$$$$/ $$$$$$/       /$$$$$$  |  ______   ______    _______ $$ |   __   ______    ______  ",
        "$$ |/$  \\$$ |  $$ |  $$ |__      $$ |        $$ |  $$/  /      \\ /      \\  /       |$$ |  /  | /      \\  /      \\ ",
        "$$ /$$$  $$ |  $$ |  $$    |     $$ |        $$ |      /$$$$$$  |$$$$$$  |/$$$$$$$/ $$ |_/$$/ /$$$$$$  |/$$$$$$  |",
        "$$ $$/$$ $$ |  $$ |  $$$$$/      $$ |        $$ |   __ $$ |  $$/ /    $$ |$$ |      $$   $$<  $$    $$ |$$ |  $$/ ",
        "$$$$/  $$$$ | _$$ |_ $$ |       _$$ |_       $$ \\__/  |$$ |     /$$$$$$$ |$$ \\_____ $$$$$$  \\ $$$$$$$$/ $$ |      ",
        "$$$/    $$$ |/ $$   |$$ |      / $$   |      $$    $$/ $$ |     $$    $$ |$$       |$$ | $$  |$$       |$$ |      ",
        "$$/      $$/ $$$$$$/ $$/       $$$$$$/        $$$$$$/  $$/       $$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$$/ $$/       ",
        "                                                                                                                 ",
        "                                                                                                                 ",
        "                                                                                                                 ",
        "                                          Author : KALEEMULLAH KHAN                                              ",
        "                                          GITHUB : https://github.com/kaleemullahkhan                            ",
        "                                                                                                                 ",
        "_________________________________________________________________________________________________________________"
    ]
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

    for line in banner_lines:
        print(Fore.CYAN + Style.BRIGHT + line)
        time.sleep(0.1)

def install_and_update_packages():
    try:
        # Update package list and install necessary packages
        print(Fore.YELLOW + "Updating package list and installing necessary packages...")
        subprocess.run("sudo apt update", check=True, shell=True)
        subprocess.run("sudo apt install -y hashcat hcxpcapngtool", check=True, shell=True)
        
        # Check if hcxpcapngtool is installed
        result = subprocess.run("hcxpcapngtool -h", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print(Fore.RED + "hcxpcapngtool is not installed. Please install it manually.")
            print(Fore.RED + "For example, you can download it from https://github.com/ZerBea/hcxtools and follow the installation instructions.")
        else:
            print(Fore.GREEN + "hcxpcapngtool is already installed.")
        
        print(Fore.GREEN + "Packages installed and updated successfully.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error during package installation/update: {e}")

def convert_to_hashcat_format(handshake_file_path, converted_file_path):
    try:
        # Command to convert .cap file to .hc22000 file using hcxpcapngtool
        command = f"hcxpcapngtool -o {converted_file_path} {handshake_file_path}"
        subprocess.run(command, check=True, shell=True)
        print(Fore.GREEN + f"File converted successfully: {converted_file_path}")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error during conversion: {e}")

def crack_handshake(converted_file_path, wordlist_path):
    try:
        # Command to run hashcat with the converted file and the wordlist
        command = f"hashcat -m 22000 {converted_file_path} {wordlist_path} --quiet"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                print(output.strip().decode())
                
        ret_code = process.poll()
        if ret_code == 0:
            print(Fore.GREEN + "Cracking process completed.")
        else:
            print(Fore.RED + f"Cracking process failed with return code {ret_code}.")
        
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error during cracking: {e}")

def main():
    clear_terminal()
    display_banner()

    # Install and update necessary packages
    install_and_update_packages()

    # Clear terminal and display banner again after package installation
    clear_terminal()
    display_banner()

    # Provide some space between banner and options
    print("\n\n")

    print(Fore.YELLOW + "Select an option:")
    print(Fore.YELLOW + "1. Crack Handshake File")
    print(Fore.YELLOW + "2. Capture Handshake File (Coming Soon)")
    
    choice = input(Fore.CYAN + "Enter your choice (1 or 2): ")
    
    if choice == '1':
        handshake_file_path = input(Fore.CYAN + "Enter the path to the handshake file (.cap): ")
        wordlist_path = input(Fore.CYAN + "Enter the path to the wordlist: ")
        
        converted_file_path = handshake_file_path.replace(".cap", ".hc22000")
        
        convert_to_hashcat_format(handshake_file_path, converted_file_path)
        crack_handshake(converted_file_path, wordlist_path)
    else:
        print(Fore.RED + "Option Not Implemented yet.")

if __name__ == "__main__":
    main()

