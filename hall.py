
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
        self.seat_list = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append('free')
            self.seat_list.append(row)
        self.seats[show_id] = self.seat_list
        
    def view_show_list(self):
        for x in self.show_list:
            print(f"Show id: {x[0]}, \t Movie: {x[1]}, \t Time: {x[2]}")
            
    def view_available_seats(self, id):
        if id not in self.seats:
            print("Wrong Show ID")
        else:
            for i in self.show_list:
                if i[0] == id:
                    print(f"Movie: {i[1]} \t\t Time: Today at {i[2]}\n\n")
                    
            for x in range(self.row):
                for y in range(self.col):
                    if(self.seats[id][x][y] == 'free'):
                        print(f'{chr(x+65)}{y+1}', end = "\t")
                    else:
                        print("X", end = "\t")
                print("\n")