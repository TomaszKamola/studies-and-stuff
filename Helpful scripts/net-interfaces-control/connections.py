import os
import subprocess as sub
from pyuac import main_requires_admin


def show_interfaces():
    output_array = sub.check_output(
        'netsh interface show interface', 
        shell=True, 
        encoding='latin-1'
    )

    return output_array

@main_requires_admin
def main():
    io = input("Chcesz włączyć czy wyłączyć interfejsy?[enable/disable]:")
    inpt = input("Jak nazywa się interfejs, który ma pozostać?:")
    
    output = os.system("wmic nic get NetConnectionID > ifcs.txt")

    with open('ifcs.txt', 'r', encoding='utf-16') as file:
        lines = file.readlines()

        extracted_ifcs = []

        for item in lines:
            if not item.startswith(' ') \
            and not item.startswith('\r') \
            and item != '':
                extracted_ifcs.append(item.strip())

        for item in extracted_ifcs[1:]:
            if item != inpt:
                os.system(f'netsh interface set interface "{item}" {io}')

    os.remove('ifcs.txt')


if __name__ == "__main__":
    print(show_interfaces())
    main()
    print(show_interfaces())
