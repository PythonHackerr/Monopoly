# file containing all lines to be printed


from player import Player


def player_lost_info(player: Player):
    print("\n" * 5)
    msg = f"{player.name()} przegral, "
    msg += f"stan konta {player.money()}."
    print(msg)
    input()


def player_won_info(player: Player):
    msg = f'Gratulacje {player.name()}, wygrales!'
    msg += ' Jestes monopolista!'
    print("\n" * 10)
    print("*" * len(msg) + "\n")
    print(msg)
    print("\n" + "*" * len(msg) + "\n" * 5)


def print_beginning():
    print("\n\nWitaj w grze monopoly!!!")
    print("Udanej zabawy na wirtualnej planszy.\n\n")
    msg = "Uwaga!!!\nDla czytelnosci planszy nazwa gracza"
    msg += " nie powinna przekraczac 7 znakow. "
    msg += "Wszystkie kolejne znaki beda usuniete!\n"
    print(msg)


def print_player_in_prison_info():
    print("Jestes w wiezieniu.")


def print_dublet_in_prison_info():
    print("Wylosowales dublet, mozesz sie ruszyc w nastepnym ruchu.")
    input()


def print_prison_possibilities_info():
    print("Nie udalo ci sie wyrzucic dubletu, nie wychodzisz z wiezienia.")
    print("Mozesz wyjsc z wiezienia za pomoca:")
    print("1. Karty WYJDZ BEZPLATNIE Z WIEZIENIA.")
    print("2. Zaplacic 50.")


def print_NT_TS_BUP(current_tile):
    '''
    Function printing everything that can be done from NormalTile,
    TrainStation or BUP tile.
    '''
    print("Co chcesz zrobic?")
    print(f"1. Kup {current_tile.name()}, koszt: {current_tile.cost()}")
    print("2. Postaw dom na wybranym polu.")
    print("3. Postaw hotel na wybranym polu.")
    print("4. Sprzedaj dom z wybranego pola.")
    print("5. Sprzedaj wszystkie domy z wybranego pola.")
    print("6. Sprzedaj hotel z wybranego pola.")
    print("7. Odkup nieruchomosc od innych graczy.")
    print("8. Pokaz stan obecny planszy.")
    print("9. Zakoncz ruch.")
    satisfied = False
    while not satisfied:
        try:
            decision = int(input("Twoja decyzja: "))
            satisfied = True
        except ValueError:
            print("Wrong input!")
    return decision


def print_CBT_Szansa():
    '''
    Function printing everything that can be done from CantBuyTile
    or Szansa tile.
    '''
    print("1. Postaw dom na wybranym polu.")
    print("2. Postaw hotel na wybranym polu.")
    print("3. Sprzedaj dom z wybranego pola.")
    print("4. Sprzedaj wszystkie domy z wybranego pola.")
    print("5. Sprzedaj hotel z wybranego pola.")
    print("6. Odkup nieruchomosc od innych graczy.")
    print("7. Pokaz stan obecny planszy.")
    print("8. Zakoncz ruch.")
    satisfied = False
    while not satisfied:
        try:
            decision = int(input("Twoja decyzja: "))
            satisfied = True
        except ValueError:
            print("Wrong input!")
    return decision


def print_player_on_parking():
    print("Stoisz na parkingu. Tracisz kolejke.")
    input()


def input_player_name():
    name = input("Podaj imie gracza: ")
    return name


def print_PlayerNameExistsInfo():
    return "Sa gracze z tym samym imieniem!"


add_player_info = "1. Dodaj kolejnego gracza\n2. Zakoncz: "


def print_wrong_input():
    print("Ups. Chyba kliknales nie to co chciales.")


def print_2_players():
    return "W grze musi byc przynajmniej dwoch graczy."


def print_wrong_tile_no_info():
    print("Podano zla wartosc.")


# build house
def print_cant_build_house():
    print("Brak mozliwosci postawienia domu na zadnym polu.")


def print_house_availables():
    print("Pola na ktorych mozesz postawic dom:")


def print_single_info(id, name):
    print(f'{id}. {name}')


chose_house_info = "Podaj numer pola na ktorym chcesz kupic dom: "


# buy hotel
def print_cant_build_hotel():
    print("Brak mozliwosci postawienia hotelu na zadnym polu.")


def print_hotel_availables():
    print("Pola na ktorych mozesz postawic hotel:")


chose_hotel_info = "Podaj numer pola na ktorym chcesz kupic hotel: "


# sell house
def print_cant_sell_house():
    print("Brak mozliwosci sprzedania domu na zadnym polu.")


def print_sell_house_availables():
    print("Pola z ktorych mozesz sprzedac dom:")


chose_house_sell_info = "Podaj numer pola z ktorego chcesz sprzedac dom: "


# sell all houses
def print_cant_sell_all_houses():
    print("Brak mozliwosci sprzedania domow na zadnym polu.")


def print_sell_all_houses_availables():
    print("Pola z ktorych mozesz sprzedac wszystkie domy:")


chose_all_houses_sell_info = "Podaj numer pola z ktorego chcesz sprzedac wszystkie domy: "


# sell hotel
def print_cant_hotel():
    print("Brak mozliwosci sprzedania hotelu na zadnym polu.")


def print_sell_hotel_availables():
    print("Pola z ktorych mozesz sprzedac hotel:")


chose_hotel_sell_info = "Podaj numer pola z ktorego chcesz sprzedac hotel: "


# prison
def print_in_prison_more_than_1(player):
    print(f"Wychodzisz z wiezienia za {player.imprisonment()} kolejki.")


def print_leave_prison_next_turn():
    print("Wychodzisz z wiezienia w nastepnym ruchu.")


decision_of_player = "Twoja decyzja: "


def print_no_cards():
    print("Nie masz kart.")


def print_leave_prison_with_card():
    print("Wychodzisz z wiezienia za pomoca karty.")


def print_no_money_4_parole():
    print("Nie stac cie na wyjscie.")


def print_leave_with_money():
    print("Wychodzisz z wiezienia za pomoca pieniedzy.")


def print_punishment_in_punishment():
    print("Podales zla wartosc, za kare nic nie mozesz juz zrobic.")


# trade
def print_cant_buy_any_tile():
    print("Brak mozliwosci kupna zadnej nieruchomosci.")


def print_tiles_available_to_buy():
    print("Pola ktore mozesz odkupic:")


choose_tile_no = "Podaj numer pola ktore chcesz kupic: "


def print_out_of_range():
    print("Podano zla wartosc")


def print_trade_info(player, current_tile, owner):
    msg = f'Gracz {player.name()} chce kupic '
    msg += f'{current_tile.name()} od {owner.name()}.'
    print(msg)
    print("Gracze ustalaja cene.")


def print_cost_proposal(player, current_tile):
    return f'{player.name()} proponuje cene za {current_tile.name()}: '


def print_wrong_offer(offer):
    print(f"Nieruchomosci nie mozna sprzedac za kwote '{offer}'")


def print_offer_discussion(owner, current_tile, offer):
    print(f'{owner.name()} czy zgadzasz sie?')
    print(f"1. Tak (sprzedaj {current_tile.name()} za {offer}).")
    print("2. Nie za taka cene.")
    print(f"3. Nie chce w ogole sprzedac {current_tile.name()}.")


def print_decision(owner):
    return f"Decyzja {owner.name()}"


def print_no_permission(current_tile):
    print(f'Brak zgody na handel polem: {current_tile.name()}')


def print_transfer_TrainStation(current_tile, rent):
    msg = f'Pole gracza {current_tile.owner().name()}, '
    msg += f'transfer: {rent}'
    print(msg)


def print_CantBuyTile_fine(current_tile):
    print(f"Zaplac {current_tile.cost()}")


def print_transfer_BUP(current_tile, rent):
    msg = f'Pole gracza {current_tile.owner().name()}, tra'
    msg += f'nsfer: {rent}'
    print(msg)


def print_some_lines():
    print("\n" * 50)


def print_player_turn_beginning(player, dice1, dice2):
    print(f"Ruch gracza: {player.info()}")
    input("Rzuc koscmi")
    print(f"Wylosowane oczka: {dice1}, {dice2}")
    return dice1, dice2


def print_get_money_start():
    print("Przechodzisz przez start. Pobierz 200.")


def print_player_position_info(player: Player, current_tile):
    print(f"\n{player.name()} jest na polu: {current_tile.name()}")


def print_rounds():
    return "Podaj liczbe tur: "


def print_rounds_more_than_0():
    return "Liczba tur musi byc wieksza od 0."


def print_winner(winners):
    msg = f'Gratulacje {winners[0].name()}, wygrales! '
    msg += f'Twoj stan konta {winners[0].money()}.'
    print("\n" * 10)
    print("*" * len(msg) + "\n")
    print(msg)
    print("\n" + "*" * len(msg) + "\n" * 5)


def print_tie_game(winners, players):
    msg = 'Remis pomiedzy'
    for player in winners:
        msg += f" {player.name()}"
    msg += f". Stan kont {players[0].money()}."
    length = len(msg)
    print("\n" * 10)
    print("*" * length + "\n")
    print(msg)
    print("\n" + "*" * length + "\n" * 5)


def print_cantbuytile():
    print("Nie mozesz kupic tego pola!")
