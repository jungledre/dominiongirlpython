#!/usr/bin/env python

import random, sqlite3

DECKS = {
    'dominion' : ["Cellar", "Chapel", "Moat", "Chancellor", "Village", "Woodcutter", "Workshop", "Bureaucrat", "Feast", "Gardens", "Militia", "Moneylender", "Remodel", "Smithy", "Spy", "Thief", "Throne Room", "Council Room", "Festival", "Laboratory", "Library", "Market", "Mine", "Witch", "Adventurer"],
    'intrigue' : ["Courtyard", "Pawn", "Secret", "Chamber", "Great Hall", "Masquerade", "Shanty Town", "Steward", "Swindler", "Wishing Well", "Baron", "Bridge", "Conspirator", "Coppersmith", "Ironworks", "Mining Village", "Scout", "Duke", "Minion", "Saboteur", "Torturer", "Trading Post", "Tribute", "Upgrade", "Harem", "Nobles"],
    'seaside' : ["Embargo", "Haven", "Lighthouse", "Native Village", "Pearl Diver", "Ambassador", "Fishing Village", "Lookout", "Smugglers", "Warehouse", "Caravan", "Cutpurse", "Island", "Navigator", "Pirate Ship", "Salvager", "Sea Hag", "Treasure Map", "Bazaar", "Explorer", "Ghost Ship", "Merchant Ship", "Outpost", "Tactician", "Treasury", "Wharf"],
    'alchemy' : ["Vineyard", "Alchemist", "Possession", "Herbalist","Philosopher's Stone","University", "Scrying Pool", "Transmute", "Apothecary", "Apprentice", "Familiar", "Golem"],
    'prosperity' : ["Loan", "Trade Route", "Watchtower", "Bishop", "Monument", "Quarry", "Talisman", "Worker's Village", "City", "Contraband", "Counting House", "Mint", "Mountebank", "Rabble", "Royal Seal", "Vault", "Venture", "Goons", "Grand Market", "Hoard", "Bank", "Expand", "Forge", "King's Court", "Peddler"],
    'cornucopia' : ["Hamlet", "Fortune Teller", "Menagerie", "Farming Village", "Horse Traders", "Remake", "Tournament", "Young Witch", "Harvest", "Horn of Plenty", "Hunting Party", "Jester", "Fairgrounds"],
    'hinterlands' : ["Crossroads", "Duchess", "Fool's Gold", "Develop", "Oasis", "Oracle", "Scheme", "Tunnel", "Jack of All Trades", "Noble Brigand", "Nomad Camp", "Silk Road", "Spice Merchant", "Trader", "Cache", "Cartographer", "Embassy", "Haggler", "Highway", "Ill-Gotten Gains", "Inn", "Mandarin", "Margrave", "Stables", "Border Village", "Farmland"],
    'darkages' : ["Madman", "Mercenary", "Spoils", "Poor House", "Beggar", "Squire", "Vagrant", "Forager", "Hermit", "Market Square", "Sage", "Storeroom", "Urchin", "Armory", "Death Cart", "Feodum", "Fortress", "Ironmonger", "Marauder", "Procession", "Rats", "Scavenger", "Wandering Minstrel", "Band of Misfits", "Bandit Camp", "Catacombs", "Count", "Counterfeit", "Cultist", "Graverobber", "Junk Dealer", "Mystic", "Pillage", "Rebuild", "Rogue", "Altar", "Hunting Grounds"],
    'guilds' : ["Candlestick Maker", "Stonemason", "Doctor", "Masterpiece", "Advisor", "Herald", "Plaza", "Taxman", "Baker", "Butcher", "Journeyman", "Merchant Guild", "Soothsayer"],
}

#Basic Cards
coin = ["Copper", "Silver", "Gold", "Platinum"]
vict = ["Estate", "Duchy", "Province", "Colony","Curse"]
other = ["Curse", "Potion"]

# 10 Cards
def give10(decknames):
    unshuffled_list = []

    for deck in decknames:
        unshuffled_list = unshuffled_list + DECKS[deck]

    i = 10

    shuffled_list = []
    while i > 0:
        r = random.randint(0, len(unshuffled_list)-1)
        shuffled_list.append(unshuffled_list[r])
        del unshuffled_list[r]
        i -= 1
        shuffled_list.sort()

    return shuffled_list

# Coin Cards
def giveCoin(decknames):
    coin_list = coin[0:3]
    if 'prosperity' in decknames:
        coin_list.append(coin[3])
    return coin_list

#Victory Cards
def giveVict(decknames):
    vict_list = vict[0:3]
    if 'prosperity' in decknames:
        vict_list.append(vict[3])
    return vict_list

# def giveOther(shuffled_list):
#     other_list = other[0]
#     # if 'witch' in shuffled_list:
#     #     other_list.append(other[0])
#     return other_list

if __name__ == "__main__":
    connection = sqlite3.connect('/Users/Westphalia/dgcards')
    list_give10 = give10(['dominion'])
    for card in list_give10:
        # print card
        cursor = connection.execute("SELECT * from tbl_cards JOIN tbl_decks ON tbl_cards.deck = tbl_decks.id where tbl_cards.name = ? ", (card,))
        print cursor.fetchone()
    #print giveCoin('dominion', 'seaside')
    #print giveVict('dominion', 'seaside')
