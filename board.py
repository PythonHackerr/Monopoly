# file containing all tiles, board, board_info
# and board printing function


from classes import (
    NormalTile,
    TrainStation,
    Szansa,
    CantBuyTile,
    BUP
)

# all tiles
start = CantBuyTile("Start")
ulica_konopacka = NormalTile("Ulica Konopacka", "brown", 60)
kasa_spoleczna1 = Szansa("Kasa spoleczna")
ulica_stalowa = NormalTile("Ulica Stalowa", "brown", 60)
podatek_dochodowy = CantBuyTile("Podatek Dochodowy", 200)
dworzec_zachodni = TrainStation("Dworzec Zachodni", 200)
ulica_radzyminska = NormalTile("Ulica Radzyminska", "blue", 100)
szansa1 = Szansa("Szansa")
ulica_jagiellonska = NormalTile("Ulica Jagiellonska", "blue", 100)
ulica_targowa = NormalTile("Ulica Targowa", "blue", 120)
wiezienie = CantBuyTile("Wiezienie")
ulica_plowiecka = NormalTile("Ulica Plowiecka", "pink", 140)
elektrownia = BUP("Elektrownia", 150)
ulica_marsa = NormalTile("Ulica Marsa", "pink", 140)
ulica_grochowska = NormalTile("Ulica Grochowska", "pink", 160)
dworzec_gdanski = TrainStation("Dworzec Gdanski", 200)
ulica_obozowa = NormalTile("Ulica Obozowa", "orange", 180)
kasa_spoleczna2 = Szansa("Kasa spoleczna")
ulica_gorczewska = NormalTile("Ulica Gorczewska", "orange", 180)
ulica_wolska = NormalTile("Ulica Wolska", "orange", 200)
bezplatny_parking = CantBuyTile("Bezplatny Parking")
ulica_mickiewicza = NormalTile("Ulica Mickiewicza", "red", 220)
szansa2 = Szansa("Szansa")
ulica_slowackiego = NormalTile("Ulica Slowackiego", "red", 220)
plac_wilsona = NormalTile("Plac Wilsona", "red", 240)
dworzec_wschodni = TrainStation("Dworzec Wschodni", 200)
ulica_swietokrzyska = NormalTile("Ulica Swietokrzyska", "yellow", 260)
krakowskie_przedmiescie = NormalTile("Krakowskie Przedmiescie", "yellow", 260)
wodociagi = BUP("Wodociagi", 150)
nowy_swiat = NormalTile("Nowy Swiat", "yellow", 280)
idz_do_wiezienia = CantBuyTile("Idz do wiezienia")
plac_trzech_krzyzy = NormalTile("Plac Trzech Krzyzy", "green", 300)
ulica_marszalkowska = NormalTile("Ulica Marszalkowska", "green", 300)
kasa_spoleczna3 = Szansa("Kasa spoleczna")
aleje_jerozolimskie = NormalTile("Aleje Jerozolimskie", "green", 320)
dworzec_centralny = TrainStation("Dworzec Centralny", 200)
szansa3 = Szansa("Szansa")
ulica_belwederska = NormalTile("Ulica Belwederska", "navy", 350)
domiar_podatkowy = CantBuyTile("Domiar Podatkowy", 100)
aleje_ujazdowskie = NormalTile("Aleje Ujazdowskie", "navy", 400)


# board
board = [
    start,
    ulica_konopacka,
    kasa_spoleczna1,
    ulica_stalowa,
    podatek_dochodowy,
    dworzec_zachodni,
    ulica_radzyminska,
    szansa1,
    ulica_jagiellonska,
    ulica_targowa,
    wiezienie,
    ulica_plowiecka,
    elektrownia,
    ulica_marsa,
    ulica_grochowska,
    dworzec_gdanski,
    ulica_obozowa,
    kasa_spoleczna2,
    ulica_gorczewska,
    ulica_wolska,
    bezplatny_parking,
    ulica_mickiewicza,
    szansa2,
    ulica_slowackiego,
    plac_wilsona,
    dworzec_wschodni,
    ulica_swietokrzyska,
    krakowskie_przedmiescie,
    wodociagi,
    nowy_swiat,
    idz_do_wiezienia,
    plac_trzech_krzyzy,
    ulica_marszalkowska,
    kasa_spoleczna3,
    aleje_jerozolimskie,
    dworzec_centralny,
    szansa3,
    ulica_belwederska,
    domiar_podatkowy,
    aleje_ujazdowskie
]


# board_info setup
board_info = {
    "brown": 0,
    "blue": 0,
    "pink": 0,
    "orange": 0,
    "red": 0,
    "yellow": 0,
    "green": 0,
    "navy": 0,
    "train_station": 0,
    "bup": 0,
    "CantBuyTile": 0,
    "szansa": 0
}


# board_info supplementation
for tile in board:
    if isinstance(tile, NormalTile):
        color = tile.color()
        board_info[color] += 1
    elif isinstance(tile, TrainStation):
        board_info["train_station"] += 1
    elif isinstance(tile, Szansa):
        board_info["szansa"] += 1
    elif isinstance(tile, BUP):
        board_info["bup"] += 1
    elif isinstance(tile, CantBuyTile):
        board_info["CantBuyTile"] += 1


# color converter en - pl for board printing function
color_converter = {
    "brown": "brazowa",
    "blue": "niebieska",
    "pink": "rozowa",
    "orange": "pomaranczowa",
    "red": "czerwona",
    "yellow": "zolta",
    "green": "zielona",
    "navy": "granatowa"
}


# board printing function
def print_board(board: list, players: list):
    head = 'Nazwa\t\t\tkoszt\t\twlasciciel\tdzielnica'
    head += '\t\tczynsz\t\tdomy\t\thotel\t\tgracze'
    print(head)
    iterator = 0
    for tile in board:
        players_on_tile = []
        for player in players:
            if player.position() == iterator:
                players_on_tile.append(player)
        iterator += 1
        if len(tile.name()) < 17:
            name = tile.name() + " " * (17 - len(tile.name()))
        else:
            name = tile.name()
        if isinstance(tile, NormalTile):
            if tile.owner() is not None:
                owner = tile.owner().name()
            else:
                owner = "brak"
            color = color_converter[tile.color()]
            if len(color) < 17:
                color = color + " " * (17 - len(color))
            line = f'{name}\t{tile.cost()}\t\t{owner}\t\t{color}\t'
            line += f'{tile.rent()}\t\t{tile.houses()}\t\t\t'
            line += f'{"tak" if tile.hotel() else "nie"}'
            for player in players_on_tile:
                line += f'\t\t{player.name()}'
            print(line)
        elif isinstance(tile, TrainStation) or isinstance(tile, BUP):
            if tile.owner() is not None:
                owner = tile.owner().name()
            else:
                owner = "brak"
            line = f'{name}\t{tile.cost()}\t\t{owner}' + "\t" * 10
            for player in players_on_tile:
                line += f'\t\t{player.name()}'
            print(line)
        elif isinstance(tile, CantBuyTile):
            line = f'{name}\t{tile.cost()}' + "\t" * 12
            for player in players_on_tile:
                line += f'\t\t{player.name()}'
            print(line)
        elif isinstance(tile, Szansa):
            line = f'{name}' + "\t" * 13
            for player in players_on_tile:
                line += f'\t\t{player.name()}'
            print(line)
