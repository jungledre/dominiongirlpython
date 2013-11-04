#!/usr/bin/env python

import random

decks = {
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

#Basic cards
coin = ["Copper", "Silver", "Gold", "Platinum"],
victory = ["Curse", "Estate", "Duchy", "Province", "Colony"],
other = ["Potion"],

def give10(*deckname):
    unshuffled_list = []
    for deckname in decks:
        unshuffled_list = unshuffled_list + decks[deckname]

    i = 10

    shuffled_list = []
    while i > 0:
        r = random.randint(0, len(unshuffled_list)-1)
        shuffled_list.append(unshuffled_list[r])
        del unshuffled_list[r]
        i -= 1
        shuffled_list.sort()

    return shuffled_list

def giveBasic(*deckname):
    coin_list = coin[1:3]
    #victory_list = victory[0:6]
    if deckname == 'prosperity':
        coin_list = coin_list.append(coin[3])
     #   victory_list = victory_list.append(victory[6])
    return coin_list
    #return victory_list

if __name__ == "__main__":

    print give10('dominion','seaside')
    print giveBasic('dominion', 'seaside')
