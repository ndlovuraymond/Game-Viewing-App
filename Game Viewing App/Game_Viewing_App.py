game_list = ['FIFA 22','FIFA 21','FORZA HORIZON 5','CALL OF DUTY: WARZONE']

game_description = [
                    "The latest installment in the world's most popular sports simulation",
                    "This is the previous installment in the game's yearly cycle",
                    "This is the latest installment in what is Raymond's favourite game franchise",
                    "This is one of the most popular FPS games in history, and one of the most adored \n" + 
                    "franchises in history, take on the online live service side of things"
                    ]

price_list = [60.00,45.00,60.00,None]

game_dictionary = dict(zip(game_list,zip(game_description,price_list)))

def view_games(random_dictionary):
    for key,value in random_dictionary.items():
        print('Game: ' + key)
        print('Description: ' + value[0])
        if value[1] == 0 or value[1] == None:
            price = 'Free'
        else:
            price = value[1]
        print('Price: ' + str(price))
        print('----------------------------------------------------------------------------------------------------')

def add_games(random_dictionary):
    name = str
    description = str
    price = float
    making_decision = True
    while making_decision:
        game_name = input('Input the game name: ')
        if len(game_name) < 3 or game_name == None:
            print('Length of name has to be equal to or greater than 3 characters.')
            continue
        elif game_name.upper() in random_dictionary:
            print("This game is already in the list so you can't add it to the list. Add a different game")
            continue
        name = game_name.upper()
        break
    while making_decision:
        game_description = input('Input the game description: ')
        if len(game_description) < 20 or game_description == None:
            print('Length of description has to be equal to or greater than 20 characters.')
            continue
        description = game_description
        break
    while making_decision:
        game_price = input('Input the game price: ')
        try :
            price = float(game_price)
            if price < 0 :
                print('Please enter a number that is equal to zero or greater')
                continue
            break
        except:
            print('Please enter a number.')
    new_game = {name.upper(): [description.capitalize(),round(price,2)]}
    random_dictionary.update(new_game)

def search(random_dictionary):
    game_search = input('What game do you want to search for?: ')
    if game_search.upper() in game_dictionary:
        print('Game: ' + game_search.upper())
        print('Description: ' + random_dictionary[game_search.upper()][0])
        print('Price: ' + str(random_dictionary[game_search.upper()][1]))
    else:
        print("This game is not in Raymond's library.")


def delete(random_dictionary):
    game_search = input('What game do you want to delete?: ')
    if game_search.upper() in game_dictionary:
        print('Game: ' + game_search.upper())
        del random_dictionary[game_search.upper()]
        print('The game has been deleted from the library.')
    else:
        print("This game is not in Raymond's library.")


print("Welcome to Raymond's game library \n")
main_menu = True
while main_menu:
    print('1. View Games \n' + '2. Search for a specific game \n'+ '3. Add Games \n'
         + '4. Delete Games \n' + '5. Quit')
    choice = input('What do you want to do?')
    if choice == '1':
        view_games(game_dictionary)
        back_to_menu = input('Press any key to return to the main menu.')
    elif choice == '2':
        search(game_dictionary)
        back_to_menu = input('Press any key to return to the main menu.')
    elif choice == '3':
        add_games(game_dictionary)
        back_to_menu = input('Press any key to return to the main menu.')
    elif choice == '4':
        delete(game_dictionary)
        back_to_menu = input('Press any key to return to the main menu.')
    elif choice == '5':
        main_menu = False
    else:
        print('You have to select an option from 1 to 5 read the menu below:)')
















