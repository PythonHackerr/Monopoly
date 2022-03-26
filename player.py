# file containing Player class


from classes import (
    NormalTile,
    TrainStation,
    CantBuyTile,
    BUP
)
from errors import (
    NoNameError,
    CantBuildHotelError,
    CantBuildHouseError,
    CantBuyTileError,
    CantSellAllHousesError,
    CantSellHotelError,
    CantSellHouseError
)
from cards import szansa_cards
from random import randint
from board import board_info
RENT0_1 = 5
RENT1_2 = 3
RENT2_3 = 2
RENT3_4 = 1.5
RENT4_HOTEL = 1.25


class Player:
    '''
    Class to represent a Player

    Attributes:
    name: str
        a name of a player
    money: int
        owned money
    owned_tiles: dict
        owned tiles by color (neighborhood)
    out_of_prison_cards: int
        number of owned out_of_prison_cards
    position: int
        index of tile player's is at
    imprisonment: int
        if greater than 0 player is in prison

    '''
    def __init__(self, name):
        if not name:
            raise NoNameError("Gracz musi miec swoja nazwe!")
        self._name = name
        self._money = 1500
        self._owned_tiles = {
            "brown": None,
            "blue": None,
            "pink": None,
            "orange": None,
            "red": None,
            "yellow": None,
            "green": None,
            "navy": None,
            "train_station": None,
            "bup": None
        }
        self._out_of_prison_cards = 0
        self._position = 0
        self._imprisonment = 0

    def name(self):
        return self._name

    def money(self):
        return self._money

    def owned_tiles(self):
        return self._owned_tiles

    def out_of_prison_cards(self):
        return self._out_of_prison_cards

    def position(self):
        return self._position

    def imprisonment(self):
        return self._imprisonment

    def buy_NormalTile(self, tile: NormalTile):
        '''
        Method that makes player buy NormalTile type tile
        if it doesn't have owner and player has enough money
        to afford it. It makes player be an owner of a tile
        and subtracts cost of a tile from player's total money.
        '''
        if tile.owner() is not None and tile.owner() != self:
            msg = f'Nie mozesz kupic, {tile.owner().name()} '
            msg += f'jest juz wlascicielem {tile.name()}.'
            raise CantBuyTileError(msg)
        if self.money() < tile.cost():
            raise CantBuyTileError("Brak funduszy.")
        if tile.owner() == self:
            msg = f'{tile.name()} nalezy juz do ciebie.'
            raise CantBuyTileError(msg)
        self._money -= tile.cost()
        colour = tile._color
        if self.owned_tiles()[colour] is None:
            self._owned_tiles[colour] = [tile]
        else:
            self._owned_tiles[colour].append(tile)
        tile._owner = self

    def buy_house(self, tile: NormalTile):
        '''
        Method that allows player to buy a house on a NormalTile
        type tile if he is the owner of a tile, there are no
        no more than 3 houses on a tile, there is no hotel
        and player can afford buying a house. Method adds
        1 house to the tile, subtracts cost of a house from
        player's money and recalculates rent of the tile.
        '''
        if not isinstance(tile, NormalTile):
            msg = f"Na {tile.name()} nie mozna stawic domu."
            raise CantBuildHouseError(msg)
        if self.money() < tile.house_cost():
            raise CantBuildHouseError("Brak funduszy.")
        if tile.houses() == 4 or tile.hotel():
            raise CantBuildHouseError("Nie mozesz dalej ulepszac nieruchomosci.")
        if tile.owner() != self:
            raise CantBuildHouseError("Nie mozesz kupic domu, nie twoje pole.")
        color = tile._color
        if len(self.owned_tiles()[color]) != board_info[color]:
            raise CantBuildHouseError("Nie mozesz kupic domu, nie masz pelnej dzielnicy.")
        self._money -= tile._house_cost
        tile._houses += 1
        if tile.houses() == 1:
            tile._rent *= RENT0_1
        elif tile.houses() == 2:
            tile._rent *= RENT1_2
        elif tile.houses() == 3:
            tile._rent *= RENT2_3
        elif tile.houses() == 4:
            tile._rent *= RENT3_4
            tile._rent = round(tile._rent)

    def buy_hotel(self, tile: NormalTile):
        '''
        Method that allows player to buy a hotel on a NormalTile
        type tile if he is the owner of a tile, there are
        4 houses, there is no hotel and player can afford
        buying a hotel. Method removes all houses from a tile,
        sets up a hotel and subtracts cost of a hotel (house) from
        player's money and recalculates rent of the tile.
        '''
        if not isinstance(tile, NormalTile):
            msg = f"Na {tile.name()} nie mozna stawic hotelu."
            raise CantBuildHotelError(msg)
        if self.money() < tile.house_cost():
            raise CantBuildHotelError("Brak funduszy.")
        if tile.houses() != 4 or tile.hotel():
            raise CantBuildHotelError("Nie mozesz zakupic hotelu.")
        if tile.owner() != self:
            raise CantBuildHotelError("Nie mozesz kupic hotelu, nie twoje pole.")
        self._money -= tile._house_cost
        tile._houses = 0
        tile._hotel = True
        tile._rent *= RENT4_HOTEL
        tile._rent = round(tile._rent)

    def sell_hotel(self, tile: NormalTile):
        '''
        Method that allows player to sell a hotel from a NormalTile
        type tile if he is the owner of a tile and there is a hotel.
        Method removes hotel from a tile and adds
        (0.5 * cost of a hotel (house)) to
        player's money and recalculates rent of the tile.
        '''
        if not isinstance(tile, NormalTile):
            msg = f"Na {tile.name()} nie moze byc hotelu."
            raise CantSellHotelError(msg)
        if not tile.hotel():
            msg = f"Nie ma hotelu na {tile.name()}."
            raise CantSellHotelError(msg)
        if tile.owner() is None:
            msg = 'Nie mozesz sprzedac hotelu. '
            msg += f'Nikt nie jest wlascicielem {tile.name()}'
            raise CantSellHotelError(msg)
        if tile.owner() != self:
            msg = 'Nie mozesz sprzedac hotelu. Wlascicielem '
            msg += f'{tile.name()} jest {tile.owner().name()}.'
            raise CantSellHotelError(msg)
        self._money += round(5 * tile._house_cost / 2)
        tile._hotel = False
        tile._rent /= (RENT0_1 * RENT1_2 * RENT2_3 * RENT3_4 * RENT4_HOTEL)
        tile._rent = round(tile._rent)

    def sell_house(self, tile: NormalTile):
        '''
        Method that allows player to sell a house from a NormalTile
        type tile if he is the owner of a tile and there is at least 1 house.
        Method removes 1 house from a tile and adds
        (0.5 * cost of a house) to player's money and
        recalculates rent of the tile.
        '''
        if not isinstance(tile, NormalTile):
            msg = f"Na {tile.name()} nie moze byc domow."
            raise CantSellHouseError(msg)
        if not tile.houses():
            msg = f"Nie ma zadnego domu na {tile.name()}."
            raise CantSellHouseError(msg)
        if tile.owner() is None:
            msg = 'Nie mozesz sprzedac domu. Nikt nie '
            msg += f'jest wlascicielem {tile.name()}'
            raise CantSellHouseError(msg)
        if tile.owner() != self:
            msg = 'Nie mozesz sprzedac domu. Wlascicielem '
            msg += f'{tile.name()} jest {tile.owner().name()}.'
            raise CantSellHouseError(msg)
        if tile.houses() == 4:
            tile._rent /= RENT3_4
        elif tile.houses() == 3:
            tile._rent /= RENT2_3
        elif tile.houses() == 2:
            tile._rent /= RENT1_2
        elif tile.houses() == 1:
            tile._rent /= RENT0_1
        tile._rent = round(tile.rent())
        tile._houses -= 1
        self._money += round(tile.house_cost() / 2)

    def sell_all_houses(self, tile: NormalTile):
        '''
        Method that allows player to sell all houses from a NormalTile
        type tile if he is the owner of a tile and there is at least 1 house.
        Method removes all houses from a tile and adds
        (0.5 * cost of a house * houses number) to player's money and
        recalculates rent of the tile.
        '''
        if not isinstance(tile, NormalTile):
            msg = f"Na {tile.name()} nie moze byc domow."
            raise CantSellAllHousesError(msg)
        if not tile.houses():
            msg = f"Nie ma zadnego domu na {tile.name()}."
            raise CantSellAllHousesError(msg)
        if tile.owner() is None:
            msg = 'Nie mozesz sprzedac domow. Nikt nie jest '
            msg += f'wlascicielem {tile.name()}'
            raise CantSellAllHousesError(msg)
        if tile.owner() != self:
            msg = 'Nie mozesz sprzedac domow. Wlascicielem '
            msg += f'{tile.name()} jest {tile.owner().name()}.'
            raise CantSellAllHousesError(msg)
        if tile.houses() == 4:
            tile._rent /= (RENT3_4 * RENT2_3 * RENT1_2 * RENT0_1)
        elif tile.houses() == 3:
            tile._rent /= (RENT2_3 * RENT1_2 * RENT0_1)
        elif tile.houses() == 2:
            tile._rent /= (RENT1_2 * RENT0_1)
        elif tile.houses() == 1:
            tile._rent /= RENT0_1
        tile._rent = round(tile.rent())
        self._money += tile.houses() * round(tile.house_cost() / 2)
        tile._houses = 0

    def calc_rent_NormalTile(self, tile: NormalTile):
        '''
        Method recalculating money after player stepping on
        other player's NormalTile tile. It adds rent to owner's
        total money and subtracts the same amount from player
        who steps on a tile.
        '''
        tile_owner = tile.owner()
        if tile_owner is None:
            return None
        self._money -= tile._rent
        tile_owner._money += tile._rent

    def buy_TrainStation(self, station: TrainStation):
        '''
        Method that makes player buy TrainStation type tile
        if it doesn't have owner and player has enough money
        to afford it. It makes player be an owner of a tile
        and subtracts cost of a tile from player's total money.
        '''
        if station.owner() is not None and station.owner() != self:
            msg = f'Nie mozesz kupic nieruchomosci {station.name()}'
            msg += f' nalezy ona do {station.owner().name()}.'
            raise CantBuyTileError(msg)
        if station.cost() > self.money():
            msg = f"Nie stac cie na {station.name()}."
            raise CantBuyTileError(msg)
        if station.owner() == self:
            msg = f"{station.name()} nalezy juz do ciebie."
            raise CantBuyTileError(msg)
        self._money -= station._cost
        if self.owned_tiles()["train_station"] is None:
            self._owned_tiles["train_station"] = [station]
        else:
            self._owned_tiles["train_station"].append(station)
        station._owner = self

    def calc_rent_TrainStation(self, station: TrainStation):
        '''
        Method recalculating money after player stepping on
        other player's TrainStation tile. It adds
        (50 * number of owned train stations by tile owner) to owner's
        total money and subtracts the same amount from player
        who steps on a tile.
        '''
        station_owner = station.owner()
        if station_owner is None:
            return None
        station_amount = len(station_owner.owned_tiles()["train_station"])
        fine = 50 * station_amount
        self._money -= fine
        station_owner._money += fine

    def pick_szansa_card(self):
        '''
        Method that randomly picks Szansa card from cards.py file.
        It adds / subtracts the amount of money that is
        written on a card. If card is WYJDZ BEZPLATNIE Z WIEZIENIA
        it is added to player's out_of_prison_cards.
        '''
        card_number = randint(1, 20)
        card = szansa_cards[card_number]
        print(card[0])
        if card[0] == "WYJDZ BEZPLATNIE Z WIEZIENIA":
            self._out_of_prison_cards += 1
        if card[0] == "Idz do wiezienia":
            self._imprisonment = 3
            self._position = 10
        self._money += card[1]

    def buy_BUP(self, bup: BUP):
        '''
        Method that makes player buy BUP type tile
        if it doesn't have owner and player has enough money
        to afford it. It makes player be an owner of a tile
        and subtracts cost of a tile from player's total money.
        '''
        if bup.owner():
            msg = f'Nie mozesz kupic nieruchomosci {bup.name()}, '
            msg += f'nalezy ona do {bup.owner().name()}.'
            raise CantBuyTileError(msg)
        if bup._cost > self._money:
            msg = f"Nie stac cie na {bup.name()}"
            raise CantBuyTileError(msg)
        self._money -= bup.cost()
        if self._owned_tiles["bup"] is None:
            self._owned_tiles["bup"] = [bup]
        else:
            self._owned_tiles["bup"].append(bup)
        bup._owner = self

    def calc_rent_BUP(self, bup: BUP, dice1, dice2):
        '''
        Method recalculating money after player stepping on
        other player's BUP tile. It adds
        (sum of dices * multiplier) to owner's
        total money and subtracts the same amount from player
        who steps on a tile.
        '''
        owner = bup.owner()
        if owner == self or owner is None:
            return None
        dice_sum = dice1 + dice2
        if len(owner.owned_tiles()["bup"]) == 1:
            multiplier = 4
        elif len(owner.owned_tiles()["bup"]) == 2:
            multiplier = 10
        transfer = dice_sum * multiplier
        self._money -= transfer
        owner._money += transfer

    def trade(self, tile, offer):
        '''
        Method allowing 2 players to trade 1 tile.
        It changes tile's owner and transfer money
        which was previously settled.
        '''
        owner = tile.owner()
        color = tile._color
        owner.owned_tiles()[color].remove(tile)
        if self.owned_tiles()[color] is None:
            self._owned_tiles[color] = [tile]
        else:
            self.owned_tiles()[color].append(tile)
        tile._owner = self
        self._money -= offer
        owner._money += offer

    def calc_money_CantBuyTile(self, cant_buy_tile: CantBuyTile):
        '''
        Method subtracting money from player if he steps on
        CantBuyTile type tile that says to pay a fine.
        '''
        self._money -= cant_buy_tile.cost()

    def info(self):
        '''
        Information about player's current status.
        '''
        return f"{self.name()}, stan konta: {self.money()}"

    def clear_tiles_owned(self):
        """
        method clearing players owned tiles
        """
        for key in self._owned_tiles.keys():
            self._owned_tiles[key] = None

    def leave_prison_dublet(self):
        """
        method used when player gets dublet in prison
        """
        self._imprisonment = 0

    def leave_prison_card(self):
        """
        method used when player leaves prison with card
        """
        self._imprisonment = 0
        self._out_of_prison_cards -= 1

    def leave_prison_money(self):
        """
        method used when player leaves prison with money
        """
        self._imprisonment = 0
        self._money -= 50

    def add_money_start(self):
        """
        method adding money for passing start
        """
        self._money += 200

    def move(self, step):
        """
        method responsible for player's movement on board
        """
        self._position += step
        self._position %= 40

    def decrement_imprisonment(self):
        """
        method decrementing player's imprisonment
        """
        self._imprisonment -= 1

    def player_gets_into_prison(self):
        """
        method used when player gets into prison
        """
        self._position = 10
        self._imprisonment = 3
