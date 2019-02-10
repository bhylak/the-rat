class Stove:
    def __init__(self):
        self.upper_right = Burner("upper_right")
        self.upper_left = Burner("upper_left")
        self.lower_left = Burner("lower_left")
        self.lower_right = Burner("lower_right")

class Burner:
    def __init__(self, name):
        self.name = name
        self.on = False
        self.pot_detected = False
        self.boiling = False
        self.temp = 0.0
    
