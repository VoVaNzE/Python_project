from dataclasses import dataclass

@dataclass
class Store:
    score: int
    dopysk: bool

    def get_score(self):
        return self.score
    
    def change_score(self,delta):
        self.score += delta


store = Store(0, False)
