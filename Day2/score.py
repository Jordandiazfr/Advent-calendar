#Player 1 
ROCK= "X"
PAPER = "Y"
SCISSOR = "Z"

#Opponent Elf 
ROCK_1 = 'A'
PAPER_2 = 'B'
SCISSOR_3 = 'C'

class Play:
    def __init__(self) -> None:
        self.total_score= 0
        self.last_played = ""
        self.shapes= {"X":1, "Y":2, "Z":3}
        self.outcomes = {"win":6 , "lost": 0, "draw":3}
       
    def score(self, p1, outcome) -> int:
        # Outcome: 0 lost, 3 draw, 6 won
        # Shape: 1 rock, 2 paper, 3 scissor
        result = self.shapes[p1] + self.outcomes[outcome]
        self.total_score = self.total_score + result
        return result

    def game(self, player: str, opponent: str) -> str:
        if opponent == ROCK_1:
            if player == SCISSOR:
                return "lost"
            if player == PAPER:
                return "win"
        if opponent == PAPER_2:
            if player == SCISSOR:
                return "win"
            if player == ROCK:
                return "lost"
        if opponent ==  SCISSOR_3:
            if player == ROCK:
                return "win"
            if player == PAPER:
                return "lost"
        return "draw"

    def strategy(self, strat: str, opponent: str): 
        method = {"X": "lost", "Y": "draw", "Z": "win"}
        player = {"rock": "X", "paper": "Y", "scissor": "Z"}
        defined_outcome = method[strat]
        for i in player.values():
            print(i)
            outcome = self.game(i, opponent)
            if  outcome == defined_outcome:
                self.last_played = i
                break
        
        self.score(self.last_played, outcome)
                
        
