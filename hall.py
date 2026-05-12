
class Hall:
    def __init__(self, hall_no, row, col):
        self.row = row
        self.col = col
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
        
    def enter_show(self, show_id, movie_name, time):
        self.tuple = (show_id, movie_name, time)
        self.show_list.append(self.tuple)