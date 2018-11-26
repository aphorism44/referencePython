'''
Created on Nov 26, 2018

@author: domje
'''

import cards, games

class BJ_Card(cards.Card):
    """A playing card used in Blackjack"""
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up:
            value = BJ_Card.RANKS.index(self.rank) + 1
            if value > 10:
                value = 10
        else:
            value = None
        return value
    
class BJ_Deck(cards.Deck):
    def populate(self):
        for suit in cards.Card.SUITS:
            for rank in cards.Card.RANKS:
                self.add(BJ_Card(rank, suit))    
            
class BJ_Hand(cards.Hand):
    """A player or dealer's hand in blackjack"""
    def __init__(self, name = "Player"):
        super(BJ_Hand, self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        total = 0
        for card in self.cards:
            total += card.value
        #now check for aces
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        if contains_ace and total <= 11:
                total += 10
        return total
    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """A blackjack player"""
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want to hit? (Y/N): ")
        return response == "y"
    def bust(self):
        print(self.name, "busts.")
        self.lose()
    def lose(self):
        print(self.name, "loses.")
    def win(self):
        print(self.name, "wins.")
    def push(self):
        print(self.name, "pushes.")
    
class BJ_Dealer(BJ_Hand):
    """A blackjack player"""
    def is_hitting(self):
        return self.total < 17
    def bust(self):
        print(self.name, "busts.")
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    """Main game loop for a blackjack game"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Dealer")
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    def play(self):
        #deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card() #hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)
        #deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)
            
        self.dealer.flip_first_card() #reveal dealer's first
        
        if not self.still_playing():
            #since all players busted, just show dealer's hand
            print(self.dealer)
        else:
            #deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)
            
            if self.dealer.is_busted():
                #everyone still playing wins
                for player in self.still_playing():
                    player.win()
            else:
                #compare all remaining players to dealer
                for player in self.still_playing():
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
            #remove everyone's cards
            for player in self.players:
                player.clear()
            self.dealer.clear()
            
                
            

if __name__ == "__main__":
    print("This is a module for playing blackjack.")
    input("\n\nPlease press Enter to exit.")