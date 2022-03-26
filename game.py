# the main file, containing whole game


from board import (
    board,
    board_info,
    print_board
)
from classes import (
    NormalTile,
    TrainStation,
    Szansa,
    CantBuyTile,
    BUP
)
from errors import (
    CantBuyTileError,
    NotEnoughTurnsError,
    NotEnoughPlayersError,
    PlayerNameExistsError
)
from player import Player
from random import randint
from interfaces import (
    input_player_name,
    player_lost_info,
    player_won_info,
    print_2_players,
    print_CantBuyTile_fine,
    print_PlayerNameExistsInfo,
    add_player_info,
    print_beginning,
    print_cant_build_hotel,
    print_cant_build_house,
    chose_hotel_info,
    chose_house_info,
    print_cant_sell_all_houses,
    print_cantbuytile,
    print_get_money_start,
    print_hotel_availables,
    print_house_availables,
    print_player_in_prison_info,
    print_dublet_in_prison_info,
    print_player_turn_beginning,
    print_prison_possibilities_info,
    print_CBT_Szansa,
    print_NT_TS_BUP,
    print_player_on_parking,
    print_rounds,
    print_rounds_more_than_0,
    print_sell_all_houses_availables,
    print_single_info,
    print_single_info,
    print_some_lines,
    print_tie_game,
    print_transfer_BUP,
    print_transfer_TrainStation,
    print_winner,
    print_wrong_input,
    print_wrong_tile_no_info
)
from interfaces import (
    print_cant_sell_house,
    print_sell_house_availables,
    chose_all_houses_sell_info,
    chose_hotel_sell_info,
    print_cant_hotel,
    print_sell_hotel_availables,
    print_in_prison_more_than_1,
    print_leave_prison_next_turn,
    print_leave_prison_with_card,
    print_leave_with_money,
    print_no_cards,
    print_no_money_4_parole,
    print_punishment_in_punishment,
    decision_of_player,
    print_cant_buy_any_tile,
    print_cost_proposal,
    print_decision,
    print_no_permission,
    print_offer_discussion,
    print_out_of_range,
    print_tiles_available_to_buy,
    print_trade_info,
    print_wrong_offer,
    choose_tile_no,
    print_player_position_info,
)


def create_players():
    '''
    Function to create players.
    '''
    players = []
    end = False
    while not end:
        name = input_player_name()
        if len(name) > 7:
            name = name[:7]
        new_player = Player(name)
        for player in players:
            if player.name() == new_player.name():
                raise PlayerNameExistsError(print_PlayerNameExistsInfo())
        players.append(new_player)
        satisfied = False
        while not satisfied:
            try:
                decision = int(input(add_player_info))
                satisfied = True
                if decision == 2:
                    end = True
            except ValueError:
                print_wrong_input()
    if len(players) < 2:
        raise NotEnoughPlayersError(print_2_players())
    return players


def throw_dice():
    '''
    Function to throw dice.
    '''
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2


def player_lost(player: Player):
    '''
    Function to remove everything what remained
    after player who lost.
    '''
    for tile in board:
        condition1 = isinstance(tile, NormalTile)
        condition2 = isinstance(tile, TrainStation)
        condition3 = isinstance(tile, BUP)
        if condition1 or condition2 or condition3:
            if tile.owner() == player:
                tile.clear_owner()
                if condition1:
                    tile.clear_houses_and_hotels()
    player.clear_tiles_owned()


def meet_conditions(sign, number, hotel_sign, player):
    """
    function to check every tile on board for given conditions
    in buy / sell house / hotel functions
    the conditions 1 and 2 are always the same
    condition 3 is tile.houses() (sign) (number)
    condition 4 is tile.hotel() is (hotel_sign)
    to have tile.hotel() is True input '+' as hotel_sign,
    otherwise input '-'
    """
    list_of_suitables = []
    for tile in board:
        # try, because not every tile has color()
        try:
            color = tile.color()
            con1 = tile.owner() == player
            con2 = len(player.owned_tiles()[color]) == board_info[color]
            if sign == "<":
                con3 = tile.houses() < number
            elif sign == "==":
                con3 = tile.houses() == number
            elif sign == ">":
                con3 = tile.houses() > number
            if hotel_sign == "+":
                con4 = tile.hotel() is True
            elif hotel_sign == "-":
                con4 = tile.hotel() is False
            if con1 and con2 and con3 and not con4:
                list_of_suitables.append(tile)
        except AttributeError:
            pass
        except TypeError:
            pass
    return list_of_suitables


def set_players_choice(msg):
    """
    function to get satisfactory player input
    """
    satisfied = False
    while not satisfied:
        try:
            chosen_tile = int(input(msg))
            satisfied = True
        except ValueError:
            print_wrong_input()
    return chosen_tile


def buy_single_house(player: Player):
    '''
    Function to let player buy a house on his tile if all conditions
    are satisfied. If buying a house is impossible, prints
    appropriate feedback.
    '''
    print()
    house_available = meet_conditions("<", 4, "+", player)
    if len(house_available) == 0:
        print_cant_build_house()
        return None
    print_house_availables()
    for tile_id in range(len(house_available)):
        house_name = house_available[tile_id].name()
        print_single_info(tile_id + 1, house_name)
    chosen_tile = set_players_choice(chose_house_info)
    try:
        player.buy_house(house_available[chosen_tile - 1])
    except IndexError:
        print_wrong_tile_no_info()


def buy_single_hotel(player: Player):
    '''
    Function to let player buy a hotel on his tile if all conditions
    are satisfied. If buying a hotel is impossible, prints
    appropriate feedback.
    '''
    print()
    hotel_available = meet_conditions("==", 4, "+", player)
    if len(hotel_available) == 0:
        print_cant_build_hotel()
        return None
    print_hotel_availables()
    for tile_id in range(len(hotel_available)):
        hotel_name = hotel_available[tile_id].name()
        print_single_info(tile_id + 1, hotel_name)
    chosen_tile = set_players_choice(chose_hotel_info)
    try:
        player.buy_hotel(hotel_available[chosen_tile - 1])
    except IndexError:
        print_wrong_tile_no_info()


def sell_single_house(player: Player):
    '''
    Function to let player sell a house from his tile if all conditions
    are satisfied. If selling a house is impossible, prints
    appropriate feedback.
    '''
    print()
    house_available = meet_conditions(">", 0, "+", player)
    if len(house_available) == 0:
        print_cant_sell_house()
        return None
    print_sell_house_availables()
    for tile_id in range(len(house_available)):
        house_name = house_available[tile_id].name()
        print_single_info(tile_id + 1, house_name)
    chosen_tile = set_players_choice(chose_house_info)
    try:
        player.sell_house(house_available[chosen_tile - 1])
    except IndexError:
        print_wrong_tile_no_info()


def sell_all_houses(player: Player):
    '''
    Function to let player sell all houses from his tile if all conditions
    are satisfied. If selling all houses is impossible, prints
    appropriate feedback.
    '''
    print()
    house_available = meet_conditions(">", 0, "+", player)
    if len(house_available) == 0:
        print_cant_sell_all_houses()
        return None
    print_sell_all_houses_availables()
    for tile_id in range(len(house_available)):
        house_name = house_available[tile_id].name()
        print_single_info(tile_id + 1, house_name)
    chosen_tile = set_players_choice(chose_all_houses_sell_info)
    try:
        player.sell_all_houses(house_available[chosen_tile - 1])
    except IndexError:
        print_wrong_tile_no_info()


def sell_single_hotel(player: Player):
    '''
    Function to let player sell a hotel from his tile if all conditions
    are satisfied. If selling a hotel is impossible, prints
    appropriate feedback.
    '''
    print()
    hotel_available = meet_conditions("==", 0, "-", player)
    if len(hotel_available) == 0:
        print_cant_hotel()
        return None
    print_sell_hotel_availables()
    for tile_id in range(len(hotel_available)):
        hotel_name = hotel_available[tile_id].name()
        print_single_info(tile_id + 1, hotel_name)
    chosen_tile = set_players_choice(chose_hotel_sell_info)
    try:
        player.sell_hotel(hotel_available[chosen_tile - 1])
    except IndexError:
        print_wrong_tile_no_info()


def turn_in_prison(player: Player, dice1, dice2):
    '''
    Function activated when player is in prison. If double on
    dice player automatically gets freedom, else he can choose
    how to try leave it.
    '''
    print_player_in_prison_info()
    if dice1 == dice2:
        print_dublet_in_prison_info()
        player.leave_prison_dublet()
        return None
    print_prison_possibilities_info()
    if player.imprisonment() > 1:
        print_in_prison_more_than_1(player)
    elif player.imprisonment() == 1:
        print_leave_prison_next_turn()
    satisfied = False
    while not satisfied:
        try:
            decision = int(input(decision_of_player))
            satisfied = True
        except ValueError:
            print_wrong_tile_no_info()
    if decision == 1:
        if player.out_of_prison_cards() == 0:
            print_no_cards()
        else:
            print_leave_prison_with_card()
            player.leave_prison_card()
    elif decision == 2:
        if player.money() < 50:
            print_no_money_4_parole()
        else:
            print_leave_with_money()
            player.leave_prison_money()
    else:
        print_punishment_in_punishment()
    input()


def buy_from_players(player: Player):
    '''
    Function responsible for trading system.
    '''
    available_tiles = []
    for tile in board:
        if isinstance(tile, BUP) or isinstance(tile, TrainStation):
            if tile.owner() is not None and tile.owner() != player:
                available_tiles.append(tile)
        elif isinstance(tile, NormalTile):
            condition1 = tile.owner() is not None
            condition2 = tile.owner() != player
            condition3 = tile.houses() == 0
            condition4 = tile.hotel()
            if condition1 and condition2 and condition3 and not condition4:
                available_tiles.append(tile)
    if len(available_tiles) == 0:
        print_cant_buy_any_tile()
        return None
    print_tiles_available_to_buy()
    for tile_id in range(len(available_tiles)):
        tile_name = available_tiles[tile_id].name()
        print_single_info(tile_id + 1, tile_name)
    chosen_tile = set_players_choice(choose_tile_no)
    try:
        current_tile = available_tiles[chosen_tile - 1]
    except IndexError:
        print_out_of_range()
        return None
    print_trade_info(player, current_tile, current_tile.owner())
    trade_settled = False
    while not trade_settled:
        print()
        offer = set_players_choice(print_cost_proposal(player, current_tile))
        if offer <= 0:
            print_wrong_offer(offer)
            trade_settled = True
            continue
        print_offer_discussion(current_tile.owner(), current_tile, offer)
        decision = set_players_choice(print_decision(current_tile.owner()))
        if decision == 1:
            player.trade(current_tile, offer)
            trade_settled = True
        elif decision == 2:
            continue
        elif decision == 3:
            print_no_permission(current_tile)
            trade_settled = True


def rent_BUP(tile: BUP, dice1, dice2):
    '''
    Function calculating transfer for stepping on BUP tile.
    '''
    owner = tile.owner()
    dice_sum = dice1 + dice2
    if len(owner.owned_tiles()["bup"]) == 1:
        multiplier = 4
    elif len(owner.owned_tiles()["bup"]) == 2:
        multiplier = 10
    transfer = dice_sum * multiplier
    return transfer


def switch_decisions_NT_TS_BUP(player, decision, players):
    '''
    Function to initialise what player chose on
    NormalTile, TrainStation or BUP tile.
    '''
    if decision == 2:
        buy_single_house(player)
    elif decision == 3:
        buy_single_hotel(player)
    elif decision == 4:
        sell_single_house(player)
    elif decision == 5:
        sell_all_houses(player)
    elif decision == 6:
        sell_single_hotel(player)
    elif decision == 7:
        buy_from_players(player)
    elif decision == 8:
        print_board(board, players)
    elif decision == 9:
        pass
    else:
        print_wrong_tile_no_info()


def switch_decisions_CBT_Szansa(player, decision, players):
    '''
    Function to initialise what player chose on
    CantBuyTile or Szansa tiles.
    '''
    if decision == 1:
        buy_single_house(player)
    elif decision == 2:
        buy_single_hotel(player)
    elif decision == 3:
        sell_single_house(player)
    elif decision == 4:
        sell_all_houses(player)
    elif decision == 5:
        sell_single_hotel(player)
    elif decision == 6:
        buy_from_players(player)
    elif decision == 7:
        print_board(board, players)
    elif decision == 8:
        pass
    else:
        print_wrong_tile_no_info()


def NormalTile_turn(current_tile: NormalTile, player, repeats, players):
    """
    function for turn on NormalTiles
    """
    condition1 = current_tile.owner() != player
    condition2 = current_tile.owner() is not None
    condition3 = repeats == 0
    if condition1 and condition2 and condition3:
        msg = f'Pole gracza {current_tile.owner().name()}, '
        msg += f'transfer: {current_tile.rent()}'
        print(msg)
        player.calc_rent_NormalTile(current_tile)
    decision = print_NT_TS_BUP(current_tile)
    if decision == 1:
        try:
            player.buy_NormalTile(current_tile)
        except CantBuyTileError:
            print_cantbuytile()
    elif decision == 9:
        return True
    else:
        switch_decisions_NT_TS_BUP(player, decision, players)


def TrainStation_turn(current_tile: TrainStation, player: Player, repeats, players):
    """
    function for turn on TrainStations
    """
    condition1 = current_tile.owner() != player
    condition2 = current_tile.owner() is not None
    condition3 = repeats == 0
    if condition1 and condition2 and condition3:
        color = "train_station"
        rent = len(current_tile.owner().owned_tiles()[color]) * 50
        print_transfer_TrainStation(current_tile, rent)
        player.calc_rent_TrainStation(current_tile)
    decision = print_NT_TS_BUP(current_tile)
    if decision == 1:
        try:
            player.buy_TrainStation(current_tile)
        except CantBuyTileError:
            print_cantbuytile()
    elif decision == 9:
        return True
    else:
        switch_decisions_NT_TS_BUP(player, decision, players)


def CantBuyTile_turn(current_tile: CantBuyTile, player: Player, repeats, players):
    """
    function for turn on CantBuyTiles
    """
    if current_tile.cost() != 0 and repeats == 0:
        print_CantBuyTile_fine(current_tile)
        player.calc_money_CantBuyTile(current_tile)
    decision = print_CBT_Szansa()
    if decision == 8:
        return True
    else:
        switch_decisions_CBT_Szansa(player, decision, players)


def BUP_turn(current_tile: BUP, player: Player, repeats, players, dice1, dice2):
    """
    function for turn on BUPs
    """
    condition1 = current_tile.owner() != player
    condition2 = current_tile.owner() is not None
    condition3 = repeats == 0
    if condition1 and condition2 and condition3:
        rent = rent_BUP(current_tile, dice1, dice2)
        print_transfer_BUP(current_tile, rent)
        player.calc_rent_BUP(current_tile, dice1, dice2)
    decision = print_NT_TS_BUP(current_tile)
    if decision == 1:
        try:
            player.buy_BUP(current_tile)
        except CantBuyTileError:
            print_cantbuytile()
    elif decision == 9:
        return True
    else:
        switch_decisions_NT_TS_BUP(player, decision, players)


def Szansa_turn(player: Player, repeats, players):
    """
    function for turn on Szansa tiles
    """
    if repeats == 0:
        player.pick_szansa_card()
    decision = print_CBT_Szansa()
    if decision == 8:
        return True
    else:
        switch_decisions_CBT_Szansa(player, decision, players)


def player_turn_beginning(player, players):
    """
    Function responsible for turns beginning.
    """
    print_some_lines()
    dice1, dice2 = throw_dice()
    print_board(board, players)
    print_player_turn_beginning(player, dice1, dice2)
    return dice1, dice2


def player_gets_money_start(player: Player):
    """
    Function giving money for crossing start.
    """
    print_get_money_start()
    player.add_money_start()


def player_turn(player: Player, players):
    '''
    Function responsible for whole player's turn.
    '''
    dice1, dice2 = player_turn_beginning(player, players)
    if player.imprisonment() > 0:
        turn_in_prison(player, dice1, dice2)
    else:
        suma = dice1 + dice2
        if player.position() + suma >= 40:
            player_gets_money_start(player)
        player.move(suma)
        current_tile = board[player.position() % 40]
        if current_tile.name() == "Idz do wiezienia":
            player.player_gets_into_prison()
        elif current_tile.name() == "Bezplatny Parking":
            print_player_on_parking()
        else:
            repeats = 0
            turn_finished = False
            while not turn_finished:
                print()
                print(player.info())
                print_player_position_info(player, current_tile)
                if isinstance(current_tile, NormalTile):
                    turn_finished = NormalTile_turn(current_tile, player, repeats, players)
                elif isinstance(current_tile, TrainStation):
                    turn_finished = TrainStation_turn(current_tile, player, repeats, players)
                elif isinstance(current_tile, CantBuyTile):
                    turn_finished = CantBuyTile_turn(current_tile, player, repeats, players)
                elif isinstance(current_tile, BUP):
                    turn_finished = BUP_turn(current_tile, player, repeats, players, dice1, dice2)
                elif isinstance(current_tile, Szansa):
                    turn_finished = Szansa_turn(player, repeats, players)
                repeats += 1
    player.decrement_imprisonment()


def set_turns():
    """
    function allowing players to set amount of turns
    """
    turns = set_players_choice(print_rounds())
    if turns < 1:
        raise NotEnoughTurnsError(print_rounds_more_than_0())
    return turns


def main_game_cycle(turns, players):
    """
    function responsible for the whole game cycle
    """
    bankrupts = []
    for turn in range(turns):
        for player in players:
            if player not in bankrupts:
                player_turn(player, players)
                if player.money() < 0:
                    player_lost_info(player)
                    player_lost(player)
                    bankrupts.append(player)
                if len(players) - len(bankrupts) == 1:
                    for player in players:
                        if player not in bankrupts:
                            player_won_info(player)
                            return bankrupts
    return bankrupts


def get_winner(players, bankrupts):
    """
    function responsible for getting and
    showing game result
    """
    # when there is one winner
    if len(players) - len(bankrupts) == 1:
        return None
    # when all turns are done and there is no winner
    biggest_money = -1000
    # check the biggest amount of money in players list
    for player in players:
        if player.money() > biggest_money:
            biggest_money = player.money()
    winners = []
    # add to winners players who have the biggest amount of money
    for player in players:
        if player.money() == biggest_money:
            winners.append(player)
    # if there is one element in winners, we have a winner
    if len(winners) == 1:
        print_winner(winners)
        return None
    # if there are more than 1 winner we have a tie
    else:
        print_tie_game(winners, players)
        return None


def game():
    '''
    Function responsible for comabining all functions needed
    '''
    print_beginning()
    all_players = create_players()
    # all_players[0].buy_NormalTile(board[1])
    # all_players[0].buy_NormalTile(board[3])
    turns = set_turns()
    bankrupts = main_game_cycle(turns, all_players)
    get_winner(all_players, bankrupts)


if __name__ == "__main__":
    game()
