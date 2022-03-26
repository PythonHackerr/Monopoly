from classes import NormalTile, TrainStation, CantBuyTile, BUP, Szansa
from errors import NoNameError, WrongColorError, WrongCostError
from player import Player
from pytest import raises


def test_player_init():
    player = Player("Jan")
    assert player._name == "Jan"
    assert player._money == 1500
    assert player._owned_tiles["brown"] is None
    assert player._owned_tiles["blue"] is None
    assert player._owned_tiles["pink"] is None
    assert player._owned_tiles["orange"] is None
    assert player._owned_tiles["red"] is None
    assert player._owned_tiles["yellow"] is None
    assert player._owned_tiles["green"] is None
    assert player._owned_tiles["navy"] is None
    assert player._owned_tiles["train_station"] is None
    assert player._owned_tiles["bup"] is None
    assert player._out_of_prison_cards == 0
    assert player._imprisonment == 0
    assert player._position == 0


def test_player_getters():
    player = Player("Jan")
    assert player.name() == "Jan"
    assert player.money() == 1500
    assert player.owned_tiles()["brown"] is None
    assert player.owned_tiles()["blue"] is None
    assert player.owned_tiles()["pink"] is None
    assert player.owned_tiles()["orange"] is None
    assert player.owned_tiles()["red"] is None
    assert player.owned_tiles()["yellow"] is None
    assert player.owned_tiles()["green"] is None
    assert player.owned_tiles()["navy"] is None
    assert player.owned_tiles()["train_station"] is None
    assert player.owned_tiles()["bup"] is None
    assert player.out_of_prison_cards() == 0
    assert player.imprisonment() == 0
    assert player.position() == 0


def test_player_no_name():
    with raises(NoNameError):
        Player("")


def test_clear_tiles_owned():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    player.buy_NormalTile(tile)
    assert len(player.owned_tiles()["brown"]) == 1
    player.clear_tiles_owned()
    assert player.owned_tiles()["brown"] is None


def test_player_leave_prison_dublet():
    player = Player("Jan")
    player._imprisonment = 3
    player.leave_prison_dublet()
    assert player.imprisonment() == 0


def test_player_leave_prison_card():
    player = Player("Jan")
    player._imprisonment = 3
    player._out_of_prison_cards = 2
    player.leave_prison_card()
    assert player.imprisonment() == 0
    assert player.out_of_prison_cards() == 1


def test_player_leave_prison_money():
    player = Player("Jan")
    player._imprisonment = 3
    player._money = 1000
    player.leave_prison_money()
    assert player.imprisonment() == 0
    assert player.money() == 950


def test_player_add_money_start():
    player = Player("Jan")
    assert player.money() == 1500
    player.add_money_start()
    assert player.money() == 1700


def test_player_move():
    player = Player("Jan")
    player._position = 38
    player.move(6)
    assert player.position() == 4


def test_decrement_imprisonment():
    player = Player("Jan")
    player._imprisonment = -3
    player.decrement_imprisonment()
    player.imprisonment() == -4


def test_player_gets_into_prison():
    player = Player("Jan")
    player.player_gets_into_prison()
    assert player.position() == 10
    assert player.imprisonment() == 3


def test_NormalTile_init():
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    assert tile._name == "Ulica Konopacka"
    assert tile._color == "brown"
    assert tile._cost == 60
    assert tile._owner is None
    assert tile._houses == 0
    assert tile._hotel is False
    assert tile._house_cost == 15
    assert tile._rent == 6


def test_NormalTile_getters():
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    assert tile.name() == "Ulica Konopacka"
    assert tile.color() == "brown"
    assert tile.cost() == 60
    assert tile.owner() is None
    assert tile.houses() == 0
    assert tile.hotel() is False
    assert tile.house_cost() == 15
    assert tile.rent() == 6


def test_clear_owner():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    player.buy_NormalTile(tile)
    assert tile.owner() == player
    tile.clear_owner()
    assert tile.owner() is None


def test_buy_and_clear_houses_and_hotel():
    player = Player("Jan")
    tile = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    assert tile.house_cost() == 15
    assert tile.rent() == 6
    player.buy_NormalTile(tile)
    player.buy_NormalTile(tile2)
    assert player.money() == 1380
    # 1st house
    player.buy_house(tile)
    assert player.money() == 1365
    assert tile.houses() == 1
    assert tile.rent() == 30
    # 2nd house
    player.buy_house(tile)
    assert player.money() == 1350
    assert tile.houses() == 2
    assert tile.rent() == 90
    # 3rd house
    player.buy_house(tile)
    assert player.money() == 1335
    assert tile.houses() == 3
    assert tile.rent() == 180
    # 4th house
    player.buy_house(tile)
    assert player.money() == 1320
    assert tile.houses() == 4
    assert tile.rent() == 270
    # buy hotel
    player.buy_hotel(tile)
    assert player.money() == 1305
    assert tile.houses() == 0
    assert tile.hotel() is True
    assert tile.rent() == 338
    tile.clear_houses_and_hotels()
    assert tile.houses() == 0
    assert tile.hotel() is False
    assert tile.rent() == 6


def test_sell_house():
    player = Player("Jan")
    ulica_konopacka = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(ulica_konopacka)
    player.buy_NormalTile(tile2)
    player.buy_house(ulica_konopacka)
    player.buy_house(ulica_konopacka)
    player.buy_house(ulica_konopacka)
    player.buy_house(ulica_konopacka)
    assert ulica_konopacka.houses() == 4
    assert player.money() == 1320
    assert ulica_konopacka.rent() == 270
    # sell 1st house
    player.sell_house(ulica_konopacka)
    assert ulica_konopacka.houses() == 3
    assert player.money() == 1328
    assert ulica_konopacka.rent() == 180
    # sell 2nd house
    player.sell_house(ulica_konopacka)
    assert ulica_konopacka.houses() == 2
    assert player.money() == 1336
    assert ulica_konopacka.rent() == 90
    # sell 3rd house
    player.sell_house(ulica_konopacka)
    assert ulica_konopacka.houses() == 1
    assert player.money() == 1344
    assert ulica_konopacka.rent() == 30
    # sell 4th house
    player.sell_house(ulica_konopacka)
    assert ulica_konopacka.houses() == 0
    assert player.money() == 1352
    assert ulica_konopacka.rent() == 6


def test_sell_all_houses():
    player = Player("Jan")
    ulica_konopacka = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(ulica_konopacka)
    player.buy_NormalTile(tile2)
    player.buy_house(ulica_konopacka)
    player.buy_house(ulica_konopacka)
    player.buy_house(ulica_konopacka)
    player.buy_house(ulica_konopacka)
    assert ulica_konopacka.houses() == 4
    assert player.money() == 1320
    assert ulica_konopacka.rent() == 270
    player.sell_all_houses(ulica_konopacka)
    assert ulica_konopacka.houses() == 0
    assert player.money() == 1352
    assert ulica_konopacka.rent() == 6


def test_sell_hotel():
    player = Player("Jan")
    ulica_konopacka = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(ulica_konopacka)
    player.buy_NormalTile(tile2)
    player.buy_house(ulica_konopacka)
    player.buy_house(ulica_konopacka)
    player.buy_house(ulica_konopacka)
    player.buy_house(ulica_konopacka)
    player.buy_hotel(ulica_konopacka)
    assert player.money() == 1305
    player.sell_hotel(ulica_konopacka)
    assert player.money() == 1305 + 38
    assert ulica_konopacka.hotel() is False
    assert ulica_konopacka.rent() == 6


def test_NormalTile_no_name():
    with raises(NoNameError):
        NormalTile("", "yellow", 50)


def test_NormalTile_wrong_color():
    with raises(WrongColorError):
        NormalTile("Ulica Konopacka", "jdhusd", 50)


def test_NormalTile_wrong_cost():
    with raises(WrongCostError):
        NormalTile("Ulica Konopacka", "yellow", -50)


def test_buy_NormalTile():
    player = Player("Jan")
    ulica_konopacka = NormalTile("Ulica Konopacka", "brown", 60)
    ulica_stalowa = NormalTile("Ulica stalowa", "brown", 100)
    player.buy_NormalTile(ulica_konopacka)
    assert player.owned_tiles()["brown"] == [ulica_konopacka]
    assert player.money() == 1440
    assert ulica_konopacka.owner() == player
    player.buy_NormalTile(ulica_stalowa)
    assert player.owned_tiles()["brown"] == [ulica_konopacka, ulica_stalowa]
    assert player.money() == 1340
    assert ulica_stalowa.owner() == player


def test_calc_rent_NormalTile():
    player = Player("Jan")
    unlucky_guy = Player("Lukasz")
    ulica_konopacka = NormalTile("Ulica Konopacka", "brown", 60)
    tile2 = NormalTile("Ulica Stalowa", "brown", 60)
    player.buy_NormalTile(ulica_konopacka)
    player.buy_NormalTile(tile2)
    assert player.money() == 1380
    unlucky_guy.calc_rent_NormalTile(ulica_konopacka)
    assert player.money() == 1386
    assert unlucky_guy.money() == 1494
    player.buy_house(ulica_konopacka)
    assert player.money() == 1371
    unlucky_guy.calc_rent_NormalTile(ulica_konopacka)
    assert player.money() == 1401
    assert unlucky_guy.money() == 1464


def test_TrainStation_init():
    dworzec = TrainStation("dworzec", 100)
    assert dworzec._name == "dworzec"
    assert dworzec._cost == 100
    assert dworzec._owner is None


def test_TrainStation_getters():
    dworzec = TrainStation("dworzec", 100)
    assert dworzec.name() == "dworzec"
    assert dworzec.cost() == 100
    assert dworzec.owner() is None


def test_TrainStation_no_name():
    with raises(NoNameError):
        TrainStation("", 100)


def test_TrainStation_wrong_cost():
    with raises(WrongCostError):
        TrainStation("dworzec", -1)


def test_buy_TrainStation():
    player = Player("Jan")
    dworzec1 = TrainStation("dworzec", 100)
    dworzec2 = TrainStation("dworzec", 200)
    assert player.owned_tiles()["train_station"] is None
    assert player.money() == 1500
    assert dworzec1.owner() is None
    player.buy_TrainStation(dworzec1)
    assert player.owned_tiles()["train_station"] == [dworzec1]
    assert player.money() == 1400
    assert dworzec1.owner() == player
    player.buy_TrainStation(dworzec2)
    assert player.owned_tiles()["train_station"] == [dworzec1, dworzec2]
    assert player.money() == 1200
    assert dworzec2.owner() == player


def test_calc_rent_TrainStation():
    owner = Player("Jan")
    unlucky_guy = Player("Lukasz")
    dworzec = TrainStation("dworzec", 100)
    dworzec2 = TrainStation("dworzec", 200)
    dworzec3 = TrainStation("dworzec", 200)
    owner.buy_TrainStation(dworzec)
    assert owner.money() == 1400
    assert unlucky_guy.money() == 1500
    # owner has 1 station, transfer: 50
    unlucky_guy.calc_rent_TrainStation(dworzec)
    assert owner.money() == 1450
    assert unlucky_guy.money() == 1450
    owner.buy_TrainStation(dworzec2)
    assert owner.money() == 1250
    # owner has 2 stations, transfer: 100
    unlucky_guy.calc_rent_TrainStation(dworzec)
    assert owner.money() == 1350
    assert unlucky_guy.money() == 1350
    # unlucky_guy on TrainStation with no owner
    unlucky_guy.calc_rent_TrainStation(dworzec3)
    assert owner.money() == 1350
    assert unlucky_guy.money() == 1350


def test_pick_szansa_card(monkeypatch):
    player = Player("Jan")

    def fake_card_number(a, b):
        return 20
    monkeypatch.setattr("player.randint", fake_card_number)
    player.pick_szansa_card()
    assert player.money() == 1600
    assert player.out_of_prison_cards() == 0


def test_pick_out_of_prison_card(monkeypatch):
    player = Player("Jan")

    def fake_card_number(a, b):
        return 2
    monkeypatch.setattr("player.randint", fake_card_number)
    player.pick_szansa_card()
    assert player.money() == 1500
    assert player.out_of_prison_cards() == 1


def test_pick_go_to_prison_card(monkeypatch):
    player = Player("Jan")

    def fake_card_number(a, b):
        return 6
    monkeypatch.setattr("player.randint", fake_card_number)
    player.pick_szansa_card()
    assert player.imprisonment() == 3
    assert player.position() == 10


def test_CantBuyTile_init():
    start = CantBuyTile("Start")
    assert start._name == "Start"
    assert start._cost == 0


def test_CantBuyTile_getters():
    start = CantBuyTile("Start")
    assert start.name() == "Start"
    assert start.cost() == 0


def test_CantBuyTile_no_name():
    with raises(NoNameError):
        CantBuyTile("")


def test_calc_money_CantBuyTile():
    player = Player("Jan")
    start = CantBuyTile("Start")
    podatek_dochodowy = CantBuyTile("Podatek Dochodowy", 200)
    assert player.money() == 1500
    player.calc_money_CantBuyTile(start)
    assert player.money() == 1500
    player.calc_money_CantBuyTile(podatek_dochodowy)
    assert player.money() == 1300


def test_BUP_init():
    wodociagi = BUP("Wodociagi", 100)
    assert wodociagi._name == "Wodociagi"
    assert wodociagi._cost == 100
    assert wodociagi._owner is None


def test_BUP_getters():
    wodociagi = BUP("Wodociagi", 100)
    assert wodociagi.name() == "Wodociagi"
    assert wodociagi.cost() == 100
    assert wodociagi.owner() is None


def test_BUP_no_name():
    with raises(NoNameError):
        BUP("", 100)


def test_BUP_wrong_cost():
    with raises(WrongCostError):
        BUP("jdias", -1)


def test_buy_BUP():
    player = Player("Jan")
    wodociagi = BUP("Wodociagi", 100)
    player.buy_BUP(wodociagi)
    assert player.money() == 1400
    assert player.owned_tiles()["bup"] == [wodociagi]
    assert wodociagi.owner() == player


def test_calc_rent_BUP():
    player = Player("Jan")
    owner = Player("Lukasz")
    wodociagi = BUP("Wodociagi", 100)
    elektrownia = BUP("Elektrownia", 150)
    owner.buy_BUP(wodociagi)
    assert owner.money() == 1400
    owner.calc_rent_BUP(wodociagi, 4, 2)
    assert owner.money() == 1400
    player.calc_rent_BUP(elektrownia, 6, 5)
    assert player.money() == 1500
    assert owner.money() == 1400
    player.calc_rent_BUP(wodociagi, 4, 2)
    assert player.money() == 1476
    assert owner.money() == 1424
    owner.buy_BUP(elektrownia)
    assert owner.money() == 1274
    player.calc_rent_BUP(elektrownia, 6, 5)
    assert player.money() == 1366
    assert owner.money() == 1384


def test_Szansa_init():
    szansa = Szansa("Szansa")
    assert szansa._name == "Szansa"


def test_Szansa_getters():
    szansa = Szansa("Szansa")
    assert szansa.name() == "Szansa"


def test_Szansa_no_name():
    with raises(NoNameError):
        Szansa("")


def test_trade():
    player = Player("Jan")
    owner = Player("Lukasz")
    ulica_konopacka = NormalTile("Ulica Konopacka", "brown", 60)
    owner.buy_NormalTile(ulica_konopacka)
    assert owner.money() == 1440
    assert owner.owned_tiles()["brown"] == [ulica_konopacka]
    assert player.owned_tiles()["brown"] is None
    assert ulica_konopacka.owner() == owner
    player.trade(ulica_konopacka, 100)
    assert player.money() == 1400
    assert owner.money() == 1540
    assert owner.owned_tiles()["brown"] == []
    assert player.owned_tiles()["brown"] == [ulica_konopacka]
    assert ulica_konopacka.owner() == player
