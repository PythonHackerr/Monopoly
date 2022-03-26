# file containing all errors


class CantBuyTileError(Exception):
    """
    raised when player wants to
    buy tile in invalid place or
    has no money
    """


class CantBuildHouseError(Exception):
    """
    raised when player wants to
    build house in invalid place
    or has no money
    """


class CantBuildHotelError(Exception):
    """
    raised when player wants to
    build hotel in invalid place
    or has no money
    """


class CantSellHotelError(Exception):
    """
    raised when player wants to
    sell hotel from invalid place
    """


class CantSellHouseError(Exception):
    """
    raised when player wants to
    sell house from invalid place
    """


class CantSellAllHousesError(Exception):
    """
    raised when player wants to
    sell all houses from invalid place
    """


class PlayerNameExistsError(Exception):
    """
    raised when given name already exists
    """


class NoNameError(Exception):
    """
    Raised when given name is empty.
    """


class WrongColorError(Exception):
    '''
    Raised when given color of tile is invalid.
    '''


class WrongCostError(Exception):
    '''
    Raised when given cost is invalid
    for example -5.
    '''


class NotEnoughTurnsError(Exception):
    '''
    Raised when given turns number is
    less than 1.
    '''


class NotEnoughPlayersError(Exception):
    '''
    Raised when there are less than 2 players
    input to the game.
    '''
