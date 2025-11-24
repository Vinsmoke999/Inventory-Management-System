Saman = []
f_name = "Saman.txt"

def load_data():
    Saman.clear()
    try:
        with open(f_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    new_item = [data[0], data[1], float(data[2]), int(data[3])]
                    Saman.append(new_item)
    except FileNotFoundError:
        pass

def save_to_file():
    with open(f_name, "w") as file:
        for item in Saman:
            line=item[0]+","+item[1]+","+str(item[2])+","+str(item[3])+"\n"
            file.write(line)

def add_Saman():
    print("ADD NEW SAMAN:-")
    saman_id = input("ENTER SAMAN ID:-")

    for item in Saman:
        if item[0] == saman_id:
            print("ID ALREADY EXISTS.:-")
            return

    name = input("ENTER SAMAN NAME:-")
    price = float(input("ENTER PRICE:-"))
    quantity = int(input("ENTER QUANTITY:-") )

    new_saman = [saman_id, name, price, quantity]
    Saman.append(new_saman)

    save_to_file()
    print("SAMAN ADDED! :-")

def show_Saman_items():
    print("SAMAN LIST:-")
    print("ID|NAME|PRICE|QUANTITY")
    print("-" * 35)

    for item in Saman:
        print(item[0]+"|"+item[1]+"|"+str(item[2])+"|"+str(item[3]))

def update_stock():
    print("UPDATE STOCK:-")
    search_id = input("ENTER SAMAN ID TO UPDATE:-")

    found = False
    for item in Saman:
        if item[0] == search_id:
            found = True
            print("CURRENT QUANTITY:" + str(item[3]) + ":-")
            print("1. ADD STOCK:-")
            print("2. SELL STOCK:-")
            choice = input("ENTER CHOICE (1 OR 2):-")

            quantity_change = int(input("ENTER QUANTITY AMOUNT:-"))

            if choice == "1":
                item[3] = item[3] + quantity_change
                print("STOCK UPDATED.:-")
            elif choice == "2":
                if item[3] >= quantity_change:
                    item[3] = item[3] - quantity_change
                    print("STOCK UPDATED.:-")
                else:
                    print("NOT ENOUGH STOCK AVAILABLE.")

            save_to_file()
            break

    if not found:
        print("SAMAN ID NOT FOUND.")

load_data()

while True:
    print("INVENTORY SYSTEM:-")
    print("1.VIEW ALL SAMAN:-")
    print("2.ADD NEW SAMAN:-")
    print("3.UPDATE STOCK:-")
    print("4.EXIT:-")

    owner_choice = input("ENTER YOUR CHOICE:-")

    if owner_choice=="1":
        show_Saman_items()
    elif owner_choice=="2":
        add_Saman()
    elif owner_choice=="3":
        update_stock()
    elif owner_choice=="4":
        print("THANKYOU!!!:-")
        break
    else:
        print("INVALID CHOICE!")
