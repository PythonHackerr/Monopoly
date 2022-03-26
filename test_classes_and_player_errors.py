from pytest import raises
from classes import NormalTile, TrainStation
from player import Player
from errors import (
    CantSellHotelError,
    CantBuildHotelError,
    CantBuildHouseError,
    CantBuyTileError,
    CantSellAllHousesError,
    CantSellHouseError
)


def test_buying_hotel_with_no_houses():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(tile)
    player.buy_NormalTile(tile2)
    with raises(CantBuildHotelError):
        player.buy_hotel(tile)


def test_build_5_houses():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(tile)
    player.buy_NormalTile(tile2)
    for i in range(4):
        player.buy_house(tile)
    assert player.money() == 1320
    assert tile.houses() == 4
    assert tile.rent() == 270
    with raises(CantBuildHouseError):
        player.buy_house(tile)


def test_buying_2nd_hotel():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(tile)
    player.buy_NormalTile(tile2)
    for i in range(4):
        player.buy_house(tile)
    player.buy_hotel(tile)
    assert player.money() == 1305
    assert tile.houses() == 0
    assert tile.hotel() is True
    assert tile.rent() == 338
    with raises(CantBuildHotelError):
        player.buy_hotel(tile)


def test_build_house_with_hotel():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(tile)
    player.buy_NormalTile(tile2)
    for i in range(4):
        player.buy_house(tile)
    player.buy_hotel(tile)
    with raises(CantBuildHouseError):
        player.buy_house(tile)


def test_buy_house_on_wrong_tile():
    dworzec = TrainStation("Dworzec", 100)
    player = Player("Jan")
    player.buy_TrainStation(dworzec)
    assert player.money() == 1400
    with raises(CantBuildHouseError):
        player.buy_house(dworzec)


def test_buy_house_no_money():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(tile)
    player.buy_NormalTile(tile2)
    player._money = 0
    with raises(CantBuildHouseError):
        player.buy_house(tile)


def test_buy_house_on_not_players_tile():
    owner = Player("Jan")
    buyer = Player("Lukasz")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    owner.buy_NormalTile(tile)
    owner.buy_NormalTile(tile2)
    owner.buy_house(tile)
    with raises(CantBuildHouseError):
        buyer.buy_house(tile)


def test_buy_house_not_full_district():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    player.buy_NormalTile(tile)
    assert player.money() == 1440
    with raises(CantBuildHouseError):
        player.buy_house(tile)


def test_buy_hotel_no_money_or_not_ur_tile():
    owner = Player("Jan")
    buyer = Player("Lukasz")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    owner.buy_NormalTile(tile)
    owner.buy_NormalTile(tile2)
    owner.buy_house(tile)
    owner.buy_house(tile)
    owner.buy_house(tile)
    owner.buy_house(tile)
    owner._money = 0
    with raises(CantBuildHotelError):
        owner.buy_hotel(tile)
    # try buying hotel, not owner
    with raises(CantBuildHotelError):
        buyer.buy_hotel(tile)


def test_buy_sell_hotel_wrong_tile():
    player = Player("Jan")
    dworzec = TrainStation("Dworzec", 200)
    player.buy_TrainStation(dworzec)
    assert player.money() == 1300
    with raises(CantBuildHotelError):
        player.buy_hotel(dworzec)
    with raises(CantSellHotelError):
        player.sell_hotel(dworzec)


def test_sell_house_with_no_houses():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(tile)
    player.buy_NormalTile(tile2)
    with raises(CantSellHouseError):
        player.sell_house(tile)


def test_sell_house_wrong_tile():
    player = Player("Jan")
    dworzec = TrainStation("Dworzec", 200)
    player.buy_TrainStation(dworzec)
    with raises(CantSellHouseError):
        player.sell_house(dworzec)


def test_sell_house_not_ur_tile():
    owner = Player("Jan")
    seller = Player("Lukasz")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    owner.buy_NormalTile(tile)
    owner.buy_NormalTile(tile2)
    owner.buy_house(tile)
    with raises(CantSellHouseError):
        seller.sell_house(tile)
    assert tile.houses() == 1
    assert seller.money() == 1500
    assert tile.owner() == owner


def test_sell_all_houses_no_houses():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(tile)
    player.buy_NormalTile(tile2)
    with raises(CantSellAllHousesError):
        player.sell_all_houses(tile)


def test_sell_all_houses_wrong_tile():
    player = Player("Jan")
    dworzec = TrainStation("Dworzec", 200)
    player.buy_TrainStation(dworzec)
    assert player.money() == 1300
    with raises(CantSellAllHousesError):
        player.sell_all_houses(dworzec)


def test_sell_all_houses_not_ur_tile():
    owner = Player("Jan")
    seller = Player("Lukasz")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    owner.buy_NormalTile(tile)
    owner.buy_NormalTile(tile2)
    owner.buy_house(tile)
    owner.buy_house(tile)
    assert tile.houses() == 2
    with raises(CantSellAllHousesError):
        seller.sell_all_houses(tile)
    assert tile.houses() == 2
    assert seller.money() == 1500
    assert tile.owner() == owner


def test_buy_NormalTile_with_owner():
    owner = Player("Jan")
    buyer = Player("Lukasz")
    ulica_konopacka = NormalTile("Ulica Konopacka", "brown", 60)
    owner.buy_NormalTile(ulica_konopacka)
    with raises(CantBuyTileError):
        buyer.buy_NormalTile(ulica_konopacka)
    assert ulica_konopacka.owner() == owner
    assert buyer.money() == 1500
    assert buyer.owned_tiles()["brown"] is None


def test_buy_NormalTile_not_enough_money():
    player = Player("Jan")
    ulica_konopacka = NormalTile("Ulica Konopacka", "brown", 6000)
    with raises(CantBuyTileError):
        player.buy_NormalTile(ulica_konopacka)
    assert player.owned_tiles()["brown"] is None
    assert player.money() == 1500
    assert ulica_konopacka.owner() is None
