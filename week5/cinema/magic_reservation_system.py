import sqlite3


class ReservationSystem:

    def __init__(self):
        self.connection = sqlite3.connect('mydb')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def show_movies(self):
        result = self.cursor.execute('''SELECT name, rating, id FROM movies ORDER BY rating''')
        for index, row in enumerate(result):
            print(
                "[{}] - {} - {} - id {} ".format(index + 1, row['name'], row['rating'], row['id']))
        self.connection.commit()

# must show how many spots are currently available
# this can be done by making a new field in
# projections table where we will save the current available seats
    def show_movie_projections(self, movie_id, date=0):
        if date == 0:
            result = self.cursor.execute(
                '''SELECT projections.type, projections.date, projections.time,
                    projections.seats, movies.name, projections.id
                    FROM projections
                    INNER JOIN movies
                    ON projections.movie_id = movies.id
                WHERE projections.movie_id = ? ORDER BY projections.time''', (movie_id,))
        else:
            result = self.cursor.execute(
                '''SELECT projections.type, projections.date, projections.time,
                    projections.seats, movies.name, projections.id
                        FROM projections
                        INNER JOIN movies
                        ON projections.movie_id = movies.id
                    WHERE projections.movie_id = ? AND projections.date = ?
                    ORDER BY projections.time''', (movie_id, date))
        for index, row in enumerate(result):
            # print(row['date'])
            print("Projections for movie {}:".format(row['name']))
            print("[{}] - {} - {} - [{}] - {} - id[{}]".format(index + 1,
                                                               row['date'], row['time'],
                                                               row['type'], row['seats'],
                                                               row['id']))
        self.connection.commit()

    def help(self):
        print('''
            These are all options you have:\n
            1)help\n
            2)show_movies\n
            3)make_reservation\n
            4)show_movie_projections <movie_id>\n
            5)finalize\n
            6)give_up\n
            7)cancel reservation <name>\n
            8)exit\n
            ''')

    def make_reservation(self, name):
        tickets = int(input("Step 1 (User): Choose number of tickets>"))
        if tickets == 'give_up':
            return False
        else:
            tickets = int(tickets)

        print("Current movies:")
        self.show_movies()
        movie_id = input("Step 2 (Movie): Choose a movie>")
        if movie_id == 'give_up':
            return False
        else:
            movie_id = int(movie_id)
        # date
        self.show_movie_projections(movie_id)
        projection_id = input("Step 3 (Projection): Choose a projection>")
        if projection_id == 'give_up':
            return False
        else:
            projection_id = int(projection_id)
        while not self.choose_projection(projection_id, tickets):
            print("There are not enought seats for this projection!")
            projection_id = int(input("Step 3 (Projection): Choose a projection>"))
        self.show_seats(projection_id)
        seats = list()
        for i in range(tickets):
            x = int(input("Choose row>"))
            y = int(input("Choose col>"))
            if self.choose_seat((x, y), name, projection_id):
                seats.append((x, y))
        print ("This is your reservation:")
        print ("Movie: {}".format(movie_id))
        print ("Seats: ".format(seats))

        final = input("Step 5 (Confirm - type 'finalize') >")
        if final == 'finalize':
            self.finalize(name, projection_id, tickets, seats)

        print("Thank you!")

    def cancel_resrvation(self, username):
        self.cursor.execute('''DELETE * FROM reservations WHERE  username = ?''', (username, ))
        self.connection.commit()

    def show_seats(self, projection_id):
        room = []
        for i in range(10):
            line = ['.'] * 10
            room.append(line)
        result = self.cursor.execute(
            '''SELECT  row, col FROM reservations WHERE projection_id = ?''', (projection_id,))
        self.connection.commit()
        for element in result:
            room[element['row']-1][element['col']-1] = 'X'
        for row in room:
            print (" ".join(row))

    def choose_seat(self, coordinates, username, projection_id):
        if((coordinates[0] < 0 or coordinates[0] > 10) or (coordinates[1] < 0 or coordinates[1] > 10)):
            print("Out of range!")
            return False
        else:
            result = self.cursor.execute(
                '''SELECT  row, col FROM reservations WHERE projection_id = ?''', (projection_id,))
            self.connection.commit()
            for coord in result:
                if coord['row'] - 1 == coordinates[0] and coord['col'] - 1 == coordinates[1]:
                    print("This seat is already taken!")
                    return False
                    # break
            # self.cursor.execute(
            #    '''INSERT INTO reservations(username, projection_id, row, col)
            #    VALUES(?, ?, ?, ?)''', (username, projection_id, coordinates[0], coordinates[1]))
            # self.connection.commit()
            return True

    def choose_projection(self, projection_id, tickets):
        result = self.cursor.execute(
            '''SELECT COUNT(?) AS taken_seats
            FROM reservations WHERE projection_id = ? ''', (projection_id, projection_id))
        result = result.fetchone()
        if result['taken_seats'] + tickets > 100:
            return False
        else:
            return True

    def finalize(self, username, projection_id, number_of_tickets, seats):
        for seat in seats:
            self.cursor.execute(
                '''INSERT INTO reservations (username, projection_id, row, col)
                    VALUES (?, ?, ?, ?)''', (username, projection_id, seat[0], seat[1]))
            self.connection.commit()


            #for cancel_reservation 
            
            result = self.cursor.execute(
                '''SELECT seats FROM projections WHERE id = ?''', (projection_id, ))
            x = result.fetchone()
            self.connection.commit()

            #when deleting a record must increase the total number of seats for projection
            self.cursor.execute(
                '''UPDATE projections SET seats =?
                WHERE id = ?''', (x['seats'] - number_of_tickets, projection_id))
            self.connection.commit()

    def main_func(self):
        name = input("Step 1 (User): Choose name>")
        print("Hello {}".format(name))
        self.help()
        while True:
            option = input("Choose something >")
            option = option.split(" ")
            if option[0] == 'exit':
                break
            elif option[0] == 'help':
                self.help()
            elif option[0] == 'show_movies':
                self.show_movies()
            elif option[0] == 'show_movie_projections':
                self.show_movie_projections(option[1])
            elif option[0] == 'finalize':
                print("You can use this option only when you make a reservation")
            elif option[0] == 'give_up':
                print("You can use this option only when you make a reservation")
            elif option[0] == 'cancel_resrvation':
                self.cancel_resrvation(option[1])
            elif option[0] == 'make_reservation':
                result = self.make_reservation(name)
                if not result:
                    break


def main():
    a = ReservationSystem()
    a.main_func()

if __name__ == '__main__':
    main()
