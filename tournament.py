import math
import random

class Tournament:
    def __init__(self):
        self.players = []
        self.rounds = []
        self.current_round = 0
        self.active = False
        self.started= False
        
    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
            return True
        return False
    
    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            return True
        return False
    def generate_bracket(self):
        random.shuffle(self.players)
        num_players = len(self.players)
        # Calculate next power of 2 for brackets slots available
        if num_players <=0:
            next_power = 0
        else:
            next_power = 2 ** math.ceil(math.log2(num_players))
        byes = next_power - num_players
        round1_matches = []
        player_pool = self.players.copy()
        #Byed players managed
        for i in range(byes):
            byed_player = player_pool.pop()
            round1_matches.append({
                "p1": byed_player,
                "p2": "BYE",
                "winner": byed_player
            })
        #Playing players managed
        while len(player_pool) >= 2:
            p1 = player_pool.pop()
            p2 = player_pool.pop()
            round1_matches.append({
                "p1": p1,
                "p2": p2,
                "winner": None
            })
        self.rounds.append(round1_matches)
        self.started = True

    def report_match(self, match_index, winner_name):
        current_matches = self.rounds[self.current_round]
        if 0 <= match_index < len(current_matches):
            match = current_matches[match_index]
            if winner_name in [match["p1"], match["p2"]]:
                match["winner"] = winner_name
                self.check_round_advancement()
                return True
        return False

    def check_round_advancement(self):
        current_matches = self.rounds[self.current_round]
        # If any match in the current round doesn't have a winner, we can't advance
        if any(m["winner"] is None for m in current_matches):
            return
        winners = [m["winner"] for m in current_matches]
        if len(winners) == 1:
            return
        next_round_matches = []

        for i in range(0, len(winners), 2):
            p1 = winners[i]
            # Handle odd number of winners if an error happened, otherwise pairs nicely
            if i+1 < len(winners):
                p2 = winners[i+1]             
            else:
                p2 = "BYE"
            next_round_matches.append({
                "p1": p1,
                "p2": p2,
                "winner": p1 if p2 == "BYE" else None
            })

        self.rounds.append(next_round_matches)
        self.current_round += 1