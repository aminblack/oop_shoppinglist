import os
from helper.exceptions import(
    WrongUserNameException,
    TypeUserNameException,
    WrongPassWordException,
    TypePassWordException,
    TypePhoneException,
    WrongPhoneNumberException,
    WrongPhoneLengthException,
    CheckUsernameException,
    CheckPasswordException
)
from auth import (Customers,
List,
Count_list,
Price_list,
Stock,
Factor
)

def clear_screen():
    """after run a code clear terminal """
    return os.system("cls")

user = Customers()
while True:
    enter = input("ENTER OR REGISTER: ").casefold()
    if enter == "register":
        rotation = 1
        while rotation == 1:
            try:
                get_username = input("enter new username: ")
                get_password = input("enter new password: ")
                get_phone = input("enter your phone: ")
                user.register(get_username, get_password, get_phone)
            except WrongPassWordException as wp:
                print(wp)
            except TypePassWordException as tp:
                print(tp)
            except WrongUserNameException as wu:
                print(wu)
            except TypeUserNameException as tu:
                print(tu)
            except TypePhoneException as tp:
                print(tp)
            except WrongPhoneNumberException as wpn:
                print(wpn)
            except WrongPhoneLengthException as wpl:
                print(wpl)
            else:
                us_ch = user.check_username(get_username)
                if us_ch == True:
                    print("username is 'repeated'")
                    continue
                with open('users.txt', 'a') as file:
                    file.write(get_username)
                    file.write('\n')
                    file.write(get_password)
                    file.write('\n')
                print("register successfully")
                rotation += 1
    else:
        try:
            username = input("enter username: ")
            password = input("enter password: ")
            user.login(username, password)
        except CheckUsernameException as cue:
            print(cue)
        except CheckPasswordException as cpe:
            print(cpe)
        print("your welcome")
        break
shopping_list = List()
count_list = Count_list()
price_list = Price_list()
while True:
    items = input("enter your items to shopping: ").casefold()
    clear_screen()
    if items == "help":
        print(shopping_list.help_list())
    elif items == "search":
        search = input("what thing you want: ").casefold()
        shopping_list.search_items(search)
    elif items == "remove":
        remove_item = input("pleas enter the item as you want remove: ").casefold()
        shopping_list.remove_list(remove_item)
        print(shopping_list)
    elif items == "edit":
        edit_item = input("enter the item in your list you want to change: ").casefold()
        new_item = input("enter the item as a new item in your list: ").casefold()
        shopping_list.edit_list(edit_item, new_item)
        print(shopping_list)
    # elif items == "price":
    #     for i in shopping_list:
    #         price = Stock.price_supply(i)
    #         price_list.append(price)
    #         print(f'price of {i} : {price} $')
    #         print(25 * "_")
    # elif items == "count":
    #     shopping = shopping_list.chose_count()
    #     x = 0
    #     while x < len(shopping_list):
    #         print(next(shopping))
    #         number = int(input("pleas enter count of this item: "))
    #         count_list.append(number)
    #         x += 1

    elif items == "exit":
        shopping_list.beautify_list(items)
        break

    else:
        shopping_list.append_repeated(items)
        print(f"we have {len(shopping_list)} items")


for i in shopping_list:
    price = Stock.price_supply(i)
    price_list.append(price)
    print(f'price of {i} : {price} $')
    print(25 * "_")

shopping = shopping_list.chose_count()
x = 0
while x < len(shopping_list):
    print(next(shopping))
    number = int(input("pleas enter count of this item: "))
    count_list.append(number)
    x += 1

Factor.final_factor(shopping_list, price_list, count_list)



