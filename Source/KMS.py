import os
import sys
import pyfiglet
import time
import socket
import itertools
from colorama import init, Fore, Back, Style

init()

def center_text(text, width):
    return text.center(width)

def center_cursor_and_text(prompt):
    console_width = os.get_terminal_size().columns
    x = (console_width - len(prompt)) // 2
    sys.stdout.write(f"\033[{x}G{prompt}")
    sys.stdout.flush()

def load_figlet_font(font="slant"):
    try:
        return pyfiglet.Figlet(font=font)
    except Exception as e:
        print(f"Ошибка загрузки шрифта: {e}")
        sys.exit(1)

def display_banner(figlet):
    banner = figlet.renderText("KMS")
    return "\n".join(center_text(line, os.get_terminal_size().columns) for line in banner.splitlines())

def display_language_menu():
    console_width = os.get_terminal_size().columns
    menu = (
        "Select language / Выберите язык:\n"
        "|─────────────────────────────────|\n"
        "1. English\n"
        "2. Русский\n"
        "|─────────────────────────────────|\n"
    )
    return "\n".join(center_text(line, console_width) for line in menu.splitlines())

def get_language_choice():
    while True:
        center_cursor_and_text("      Select language 1/2: ")
        choice = input().strip()
        if choice in ["1", "2"]:
            return choice
        print("Invalid input. Try again.")

def display_main_menu(lang):
    console_width = os.get_terminal_size().columns
    if lang == "1":
        menu = (
            "Select an activation command:\n"
            "|────────────────────────────────────────────────────────────────────────|\n"
            "1. Start activation\n"
            "2. Deactivate Windows\n"
            "3. Complete activation\n"
            "4. Check activation status\n"
            "|────────────────────────────────────────────────────────────────────────|\n"
            "5. Key for Windows 11 Pro or Windows 10 Pro for Workstations\n"
            "6. Key for Windows 11 Pro or Windows 10 Pro (Any device)\n"
            "7. Key for Windows 11 or Windows 10 LTSC 2024, 2021, 2019 (LTSC)\n"
            "|────────────────────────────────────────────────────────────────────────|\n"
            "8. About program\n"
            "0. Exit the program\n"
        )
    else:
        menu = (
            "Выберите команду для активации:\n"
            "|────────────────────────────────────────────────────────────────────────|\n"
            "1. Начать активацию\n"
            "2. Деактивировать Windows\n"
            "3. Завершить активацию\n"
            "4. Проверить статус активации\n"
            "|────────────────────────────────────────────────────────────────────────|\n"
            "5. Ключ для Windows 11 Pro или Windows 10 Pro for Workstations\n"
            "6. Ключ для Windows 11 Pro или Windows 10 Pro (Любое устройство)\n"
            "7. Ключ для Windows 11 или Windows 10 LTSC 2024, 2021, 2019 (LTSC)\n"
            "|────────────────────────────────────────────────────────────────────────|\n"
            "8. О программе\n"
            "0. Выйти из программы\n"
        )
    return "\n".join(center_text(line, console_width) for line in menu.splitlines())

def execute_command(command):
    print(f"\nExecuting command: {command}")
    os.system(command)

def log_action(action):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {action}\n")

def test_connection(server="kms.digiboy.ir", port=1688):
    try:
        socket.create_connection((server, port), timeout=5)
        print(center_text(Fore.GREEN + "Connection to KMS server successful!" + Style.RESET_ALL, os.get_terminal_size().columns))
        return True
    except Exception as e:
        print(center_text(Fore.RED + "Failed to connect to KMS server!" + Style.RESET_ALL, os.get_terminal_size().columns))
        print(f"Error: {e}")
        return False

def display_about():
    about_text = (
        "This program was created for educational purposes.\n"
        "Author: VTMEEN\n"
        "Version: 1.0\n"
        "Source: https://docs.microsoft.com/ru-ru/windows-server/get-started/kms-client-activation-keys"
    )
    print("\n".join(center_text(line, os.get_terminal_size().columns) for line in about_text.splitlines()))

def show_progress_bar(duration=0.5):
    bar_length = 20
    for i in range(bar_length + 1):
        progress = f"[{'#' * i}{'.' * (bar_length - i)}] {int(i / bar_length * 100)}%"
        sys.stdout.write(f"\r{center_text(progress, os.get_terminal_size().columns)}")
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    print() 

def show_loading_animation(text="Loading", duration=3):
    end_time = time.time() + duration
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    while time.time() < end_time:
        sys.stdout.write(f"\r{center_text(f'{text} {next(spinner)}', os.get_terminal_size().columns)}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * os.get_terminal_size().columns) 
    sys.stdout.flush()
    print()

def check_activation_status():
    print() 
    print(center_text("Checking activation status...", os.get_terminal_size().columns))
    os.system("slmgr /dli")
    os.system("slmgr /xpr")

def main():
    if os.name != 'nt':
        print("This program is designed for Windows.")
        sys.exit(1)


    show_loading_animation("Initializing", duration=3)

    
    if not os.environ.get("USERNAME") == "Administrator":
        warning_message = (
            Fore.YELLOW + Back.BLACK +
            "                 Warning: It is recommended to run the program as Administrator.\n" +
            "         Предупреждение: Рекомендуется запускать программу от имени администратора." +
            Style.RESET_ALL
        )
        print("\n".join(center_text(line, os.get_terminal_size().columns) for line in warning_message.splitlines()))

    figlet = load_figlet_font()
    print(display_banner(figlet))

    print(display_language_menu())
    lang_choice = get_language_choice()
    os.system('cls' if os.name == 'nt' else 'clear')

    print(display_banner(figlet))
    print(display_main_menu(lang_choice))

    while True:
      
        print()

        center_cursor_and_text("     Enter your choice: ")
        choice = input().strip()
        
    
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            show_progress_bar(duration=0.5)  
        if choice == "1":
            print()  
            print(center_text("Activating Windows... This may take a few moments.", os.get_terminal_size().columns))
            if test_connection():
                execute_command("slmgr /skms kms.digiboy.ir")
                log_action("Connected to KMS server")
        elif choice == "2":
            print() 
            print(center_text("Deactivating Windows... Please wait.", os.get_terminal_size().columns))
            execute_command("slmgr /upk")
            log_action("Deactivated Windows")
        elif choice == "3":
            print()  
            print(center_text("Completing activation...", os.get_terminal_size().columns))
            execute_command("slmgr /ato")
            log_action("Activated Windows")
        elif choice == "4":
            check_activation_status()
            log_action("Checked activation status")
        elif choice == "5":
            execute_command("slmgr /ipk NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J")
            log_action("Used Pro Workstation key")
        elif choice == "6":
            execute_command("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            log_action("Used Pro Devices key")
        elif choice == "7":
            execute_command("slmgr /ipk M7XTQ-FN8P6-TTKYV-9D4CC-J462D")
            log_action("Used LTSC key")
        elif choice == "8":
            display_about()
            log_action("Displayed About section")
        elif choice == "0":
            message = "Exiting program." if lang_choice == "1" else "   Выход из программы."
            print(center_text(message, os.get_terminal_size().columns))
            log_action("Exited program")
            break
        else:
            error_message = "Invalid input. Try again." if lang_choice == "1" else "Некорректный ввод. Попробуйте снова."
            print(Back.RED + Fore.WHITE + center_text(error_message, os.get_terminal_size().columns) + Style.RESET_ALL)
       
if __name__ == "__main__":
    main()
