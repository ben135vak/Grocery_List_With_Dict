def view_items(goods):
    for good in goods:
        print(good + " Amount: " + str(goods.get(good)))


def is_in_the_list(product, goods):
    in_the_list = 0
    for good in goods:
        if product.casefold() == good.casefold():
            in_the_list = 1
            break
    if in_the_list == 1:
        print(product + " In The List")

    else:
        print(product + " Not In The List")


def how_many(product, goods):
    count = 0
    for good in goods:
        if good == product.casefold():
            return goods.get(good)
    return 0


def remove_item(product, goods):
    if product.casefold() in goods.keys():
        del goods[product.casefold()]
    else:
        print("Item Is Not In The List")


def remove_item_once(product, goods):
    global the_list
    if product.casefold() not in goods.keys() or goods.get(product) <= 0:
        print("You don't have the product in you cart")
    else:
        sub_from = goods.get(product)
        the_list[product.casefold()] = sub_from - 1
    if goods.get(product) <= 0:
        remove_item(product,goods)


def add_item(product, goods):
    global the_list
    if product.casefold() in goods.keys():
        add_to = goods.get(product)
        the_list[product.casefold()] = add_to + 1
    else:
        the_list.update({product.casefold(): 1})


def print_no_good_entries(goods):
    for good in goods:
        if len(good) < 3:
            print(good)
            continue
        else:
            for character in good:
                if character.isdigit():
                    print(good)
                    break


def check_popular_items(goods):
    popular_list = []
    item_with_count = ""
    count_items = 0
    for good in goods:
        count = how_many(good, goods)
        if count_items < 3:
            count_items += 1
            item_with_count = str(count) + "-" + good.upper()
            if item_with_count in popular_list:
                continue
            else:
                popular_list.append(item_with_count)

    for popular in popular_list:
        print(popular)


def get_total_sum(goods):
    count = 0
    for key in goods.keys():
        count += goods.get(key)

    print(count)


def login():
    global the_list
    global data_base_of_users
    print("Please Login: ")
    username = input().casefold()

    if username in data_base_of_users:
        the_list = data_base_of_users.get(username)
    else:
        the_list = {}
        data_base_of_users.update({username: the_list})


ans = 0

data_base_of_users = {}
the_list = {}
login()
the_input = input("Enter the Items: ")
the_products = the_input.split(",")

for the_product in the_products:
    the_list.update({the_product.casefold(): 1})

while ans != -1:
    print("1) Watch The Goods in the list")
    print("2) check amount of items in the list")
    print("3) Check if a item is in the list")
    print("4) Check amount of product in the list")
    print("5) Remove item from the list")
    print("6) Remove an Item Completely")
    print("7) Add Item To the list")
    print("8) print all non valid entries")
    print("9) Total delete of items")
    print("10) Watch popular items (Top 3)")
    print("11) Total Sum Of Products")
    print("12) Exit")
    print("13) Log Out")
    print("14) Save To Text File")
    print("15) Save To CSV File")
    ans = int(input("What Do You Want To Do? "))
    print("\n")
    if ans == 1:
        view_items(the_list)
    elif ans == 2:
        print(len(the_list))
    elif ans == 3:
        is_in_the_list(input("Enter Product Name: ").casefold(), the_list)
    elif ans == 4:
        print(how_many(input("Enter Product Name: ").casefold(), the_list))
    elif ans == 5:
        remove_item_once(input("Enter Product Name: ").casefold(), the_list)
    elif ans == 6:
        remove_item(input("Enter Product Name: ").casefold(), the_list)
    elif ans == 7:
        add_item(input("Enter Product Name: ").casefold(), the_list)
    elif ans == 8:
        print_no_good_entries(the_list)
    elif ans == 9:
        the_list.clear()
    elif ans == 10:
        check_popular_items(the_list)
    elif ans == 11:
        get_total_sum(the_list)
    elif ans == 12:
        ans = -1
    elif ans == 13:
        login()
    elif ans == 14:
        file = open("My List.txt", "W")
        file.write(the_list)
        file.close()
    elif ans == 15:
        file = open("My List.csv", "W")
        file.write(the_list)
        file.close()

    else:
        print("Please Enter Valid Entry")
    print("Done!\n")
