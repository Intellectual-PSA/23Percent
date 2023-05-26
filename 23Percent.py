class Paper:
    def __init__(self, paper_id, total_score=100):
        self.paper_id = paper_id
        self.total_score = total_score
        self.score = 0

    def grade(self):
        self.score = self.total_score * 0.23

    def display_score(self):
        print(f"Paper ID: {self.paper_id}, Score: {self.score} out of {self.total_score}")


# Create a paper
paper1 = Paper('paper1')

# Grade the paper
paper1.grade()

# Display the score
paper1.display_score()
