from comm import update_money, extract_money, extract_deals, update_deals

STARTING_AMOUNT = 15000  # 1,000 = 1 Million.
money = {}
deals = {}
number_of_players = input("Enter the number of players: ")
number_of_players = int(number_of_players)

def initialise_money(number_of_players):
    for x in range(number_of_players):
        name = input(f"Enter the name of player {x + 1}: ")
        money[name] = STARTING_AMOUNT
    update_money(money)
    ask()

def print_details():
    details = extract_money()
    for key, value in details.items():
        cash = value
        if cash < 1000:
            print(f"{key}:\t{value}k")
        else:
            print(f"{key}:\t{value / 1000}M")

def print_deals():
    deals = extract_deals()
    for player, player_deals in deals.items():
        print(f"Deals for {player}:")
        for i, deal in enumerate(player_deals, 1):
            print(f"  {i}. {deal}")

def ask():
    ans = input("Do you want to view your cash(*), add(+), subtract(-), record a deal(d), view the deals(v) or remove a deal(r)? ")
    if ans != "exit":
        if ans == "+":
            player_name = input("Enter the player name: ")
            amount = int(input(f"Enter the amount to add for {player_name}: "))
            if player_name in money:
                money[player_name] += amount
                update_money(money)
                print(f"{amount}k added to {player_name}.")
            else:
                print(f"No player found with name {player_name}.")
        if ans == "-":
            player_name = input("Enter the player name: ")
            amount = int(input(f"Enter the amount to subtract for {player_name}: "))
            if player_name in money:
                if money[player_name] >= amount:
                    money[player_name] -= amount
                    update_money(money)
                    print(f"{amount}k subtracted from {player_name}.")
                else:
                    print(f"Not enough funds. {player_name} has only {money[player_name]}k.")
            else:
                print(f"No player found with name {player_name}.")
        if ans == "*":
            print_details()
        if ans == "d":
            player_name = input("Enter the player name: ")
            deal = input(f"Enter the deal for {player_name}: ")
            if player_name in deals:
                deals[player_name].append(deal)
            else:
                deals[player_name] = [deal]
            update_deals(deals)
            print(f"Deal recorded for {player_name}.")
        if ans == "r":
            player_name = input("Enter the player name: ")
            if player_name in deals and deals[player_name]:
                print(f"Deals for {player_name}:")
                for i, deal in enumerate(deals[player_name], 1):
                    print(f"  {i}. {deal}")
                deal_index = int(input("Enter the number of the deal to remove: ")) - 1
                if 0 <= deal_index < len(deals[player_name]):
                    removed_deal = deals[player_name].pop(deal_index)
                    update_deals(deals)
                    print(f"Removed deal: {removed_deal}")
                else:
                    print("Invalid deal number.")
            else:
                print(f"No deals found for {player_name}.")
        if ans == "v":
            print_deals()
        loopin()

def loopin():
    try:
        ask()
    except KeyboardInterrupt:
        print("Goodbye...")

initialise_money(number_of_players)
