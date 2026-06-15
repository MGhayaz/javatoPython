import random

def game():
    score = random.randint(1,100)
    with open("ch9Question2TextFile.txt") as f:
        hi_score = f.read()
        if(hi_score != ""):
            hi_score = int(hi_score)
        else : 
            hi_score = 0

        
        if(hi_score < score):
            with open("ch9Question2TextFile.txt", "w") as f:
                f.write(str(score))
            print(f"new high score {score} and former highscore {hi_score}")    
        return score        

game()