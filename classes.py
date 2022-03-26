# file containing all tile types classes


from errors import (
    NoNameError,
    WrongColorError,
    WrongCostError
)


class Tile:
    """
    Class to represent a tile

    Attributes:
    name: str
        name of a tile
    """
    def __init__(self, name):
        if not name:
            raise NoNameError
        self._name = name

    def name(self):
        return self._name


class Tile_with_cost(Tile):
    """
    Class to represent all classes with cost
    Class inherites name after Tile

    Attributes:
    cost: int
        cost of a tile
    """
    def __init__(self, name, cost):
        super().__init__(name)
        if cost <= 0:
            raise WrongCostError
        self._cost = cost

    def cost(self):
        return self._cost


class NormalTile(Tile_with_cost):
    '''
    Class to represent tiles with neighborhood
    Class inherites name and cost after Tile_with_cost

    Attributes:
    color: str
        color of neighborhood
    owner: Player
        owner of the tile
    houses: int
        number of houses on tile
    hotel: bool
        info whether hotel is on the tile
    house_cost: int
        the cost of a house on the tile
    rent: int
        money transfered between players if tile gets stepped on
    '''
    def __init__(self, name, color, cost):
        super().__init__(name, cost)
        colors = ["brown", "blue", "pink", "orange",
                  "red", "yellow", "green", "navy"]
        if color not in colors:
            raise WrongColorError
        self._color = color
        self._owner = None
        self._houses = 0
        self._hotel = False
        self._house_cost = round(self._cost / 4)
        self._rent = round(self._cost / 10)

    def color(self):
        return self._color

    def owner(self):
        return self._owner

    def houses(self):
        return self._houses

    def hotel(self):
        return self._hotel

    def house_cost(self):
        return self._house_cost

    def rent(self):
        return self._rent

    def clear_owner(self):
        self._owner = None

    def clear_houses_and_hotels(self):
        if self.hotel():
            self._rent /= 56.25
        elif self.houses() == 4:
            self._rent /= 45
        elif self.houses() == 3:
            self._rent /= 30
        elif self.houses() == 2:
            self._rent /= 15
        elif self.houses() == 1:
            self._rent /= 5
        self._rent = round(self.rent())
        self._hotel = False
        self._houses = 0


class TrainStation(Tile_with_cost):
    '''
    Class to represent tiles with train station
    Class inherites name and cost after Tile_with_cost

    Attributes:
    name: str
        name of a tile
    color: str
        color is "train_station"
    owner: Player
        owner of the tile
    cost: int
        money needed to buy a tile
    '''
    def __init__(self, name, cost):
        super().__init__(name, cost)
        self._owner = None
        self._color = "train_station"

    def owner(self):
        return self._owner

    def clear_owner(self):
        self._owner = None


# All tiles which cannot be bought, except Szansa tiles
class CantBuyTile(Tile):
    '''
    Class to represent tiles which cannot be bought
    Class inherites name after Tile

    Attributes:
    cost: int
        money removed from player's total money when stepping on tile
    '''
    def __init__(self, name, cost=0):
        super().__init__(name)
        self._cost = cost

    def cost(self):
        return self._cost


# budynki uzytecznosci publicznej - BUP
class BUP(Tile_with_cost):
    '''
    Class to represent budynki uzytecznosci publicznej tiles
    Class inherites name and cost after Tile_with_cost

    Attributes:
    owner: Player
        owner of the tile
    color: str
        color is "bup"
    '''
    def __init__(self, name, cost):
        super().__init__(name, cost)
        self._owner = None
        self._color = "bup"

    def owner(self):
        return self._owner

    def clear_owner(self):
        self._owner = None


class Szansa(Tile):
    '''
    Class to represent Szansa and Kasa spoleczna tiles
    Class inherites name after Tile
    '''
    def __init__(self, name):
        super().__init__(name)
