
import time
import colorama
from colorama import Fore
from colorama import Style
colorama.init()


numbers = {}


class phonBook:
    #  phoneBook constuctor
    def __init__(self, name, PhoneNumber, gmail):
        self.name = name
        self.PhoneNumber = PhoneNumber
        self.gmail = gmail

    def AddNewNumberAndGmail(self):
        numbers[self.name] = self.PhoneNumber, self.gmail
        print(Fore.BLUE + "Added Successfully..." + Style.RESET_ALL)


    def RemoveNumberAndGmail(self):
        self.name = input("Enter name which you wan to delete: ").title()
        if self.name in numbers:
            del numbers[self.name]
        else:
            print(Fore.RED + "File not found" + Style.RESET_ALL)



    def ShowDetai(self):
        for key in numbers.keys():
            print("Number:", key, "\tPhone:", numbers[key][0], "\tGmail:", numbers[key][1])


    def LookUp(self):
        print("Look up :")
        self.name = input("Input Your LookUp NAme:").title()
        if self.name in numbers:
            print("Number:", numbers[self.name][0], '\tGmail', numbers[self.name][1])

        else:
            print(Fore.RED + "Contact not found" + Style.RESET_ALL)



def print_menu():

    print(Fore.GREEN + "\n   *** Phone Book Menu ***\n" +
          "------------------------------------------\n" +
          "Enter 1,2,3,4 or 5:\n" +
          "Enter 1 To Add a New contact record\n" +
          "Enter 2 To Show Numbers\n" +
          "Enter 3 To search your contacts\n" +
          "Enter 4 To Delete a Number\n"+
          "Enter 5 To Quit\n**********************" + Style.RESET_ALL)
    time.sleep(0.1)


if __name__ == "__main__":


    menu_choice = 0
    while menu_choice != 5:
        print_menu()
        print("Please Enter a choice(1-5) :", end="")

        time.sleep(0.1)

        try:
            menu_choice = int(input())
        except ValueError as e:
            print(Fore.MAGENTA + "Please Try again.." + Style.RESET_ALL)


        if menu_choice == 1:
            phonDetail = phonBook(input("Name: ").title(), input("Phone Number: ").capitalize(),
                                  input("Gmail account: ").capitalize())
            phonDetail.AddNewNumberAndGmail()

        elif menu_choice == 2:
            try:
                phonDetail.ShowDetai()
            except NameError as e:
                print(Fore.CYAN + "Your phone book is totally empty" + Style.RESET_ALL)


        elif menu_choice == 3:
            try:
                phonDetail.LookUp()
            except NameError as e:
                print(Fore.CYAN + "Your phonebook is empty or Invalid name.." + Style.RESET_ALL)


        elif menu_choice == 4:
            try:
                phonDetail.RemoveNumberAndGmail()
            except NameError as e:
                print(Fore.CYAN + "Your phonebook is empty or Invalid name.." + Style.RESET_ALL)


        elif menu_choice >= 5:
            break
            print_menu()