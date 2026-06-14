import pymysql as ps
import datetime

flights = ps.connect(user='root', password='tiger', host='localhost')
mycursor = flights.cursor()

def setup():
    mycursor.execute("create database f2")
    print("Database Created")

    mycursor.execute("use f2")
    print("Database used\n")

    tickets = """create table Tickets(
        T_no int(5),
        Name char(20),
        Date varchar(5),
        Source char(20),
        Destination char(20),
        Seat_class char(10),
        Seat_price int(4),
        Luggage_price int(4),
        Total_amt varchar(10)
    )"""
    mycursor.execute(tickets)
    flights.commit()
    print("Information Table Created\n")

    seat = "create table Seat(Class char(20), Price varchar(10))"
    mycursor.execute(seat)

    row = "insert into Seat(Class, Price) values(%s, %s)"
    mycursor.execute(row, ["First Class", "Rs 6000/-"])
    mycursor.execute(row, ["Business Class", "Rs 4000/-"])
    mycursor.execute(row, ["Economy Class", "Rs 2000/-"])
    flights.commit()
    print("Seat Rate Card Created\n")

    luggage = "create table Luggage(Weight varchar(6), Price_per_kg varchar(6))"
    mycursor.execute(luggage)

    row_l = "insert into Luggage(Weight, Price_per_kg) values(%s, %s)"
    mycursor.execute(row_l, ["<=10kg", "Rs 100"])
    mycursor.execute(row_l, ["<=20kg", "Rs 150"])
    mycursor.execute(row_l, [">20kg", "Rs 200"])
    flights.commit()
    print("Luggage Rate Card Created\n")


def register():
    global t
    L = [t]

    name = input("Enter name: ")
    L.append(name)

    date = input("Enter Date of journey (dd/mm): ")
    L.append(date)

    source = input("Enter source: ")
    L.append(source)

    destination = input("Enter destination: ")
    L.append(destination)

    sql = "insert into Tickets(T_no, Name, Date, Source, Destination) values(%s, %s, %s, %s, %s)"
    mycursor.execute(sql, L)
    flights.commit()

    print("\nPassenger Registered")
    print("Your ticket number is:", t)
    print("Remember it for booking your flight!\n")


def seatclass():
    a = input("Please enter your Ticket Number: ")

    sql = "select * from Seat"
    mycursor.execute(sql)
    rows = mycursor.fetchall()

    print("Rate of the seats are:-")
    print("Class\t\tPrice")
    print("--------------------------")

    for i in rows:
        print(i[0], "\t", i[1])

    print("\nThe following seats are available for you:-")
    print("First class - Enter 1")
    print("Business class - Enter 2")
    print("Economy class - Enter 3")

    x = int(input("Enter Your Choice Please: "))

    if x == 1:
        print("You have opted First class")
        seat_class = "First"
        seat_price = 6000
    elif x == 2:
        print("You have opted Business class")
        seat_class = "Business"
        seat_price = 4000
    elif x == 3:
        print("You have opted Economy class")
        seat_class = "Economy"
        seat_price = 2000
    else:
        print("Please choose a valid Class")
        return

    c = "update Tickets set Seat_class=%s where T_no=%s"
    p = "update Tickets set Seat_price=%s where T_no=%s"

    mycursor.execute(c, (seat_class, a))
    mycursor.execute(p, (seat_price, a))
    flights.commit()

    print("Your seat bill is:", seat_price, "\n")


def luggagebill():
    a = input("Please enter your Ticket Number: ")

    print("The rate for luggage is:")
    sql = "select * from Luggage"
    mycursor.execute(sql)
    rows = mycursor.fetchall()

    print("Extra Weight\tPrice/kg")
    print("--------------------------")

    for i in rows:
        print(i[0], "\t", i[1])

    y = int(input("Enter Your weight of extra luggage: "))

    if y <= 10:
        z = y * 100
    elif 10 < y <= 20:
        z = y * 150
    else:
        z = y * 200

    update = "update Tickets set Luggage_price=%s where T_no=%s"
    mycursor.execute(update, (z, a))
    flights.commit()

    print("Your luggage bill is: Rs", z, "\n")


def ticketamount():
    a = input("Please enter your Ticket Number: ")

    sql_s = "select Seat_price from Tickets where T_no=%s"
    mycursor.execute(sql_s, a)
    sp = mycursor.fetchall()
    s = int(sp[0][0])

    sql_l = "select Luggage_price from Tickets where T_no=%s"
    mycursor.execute(sql_l, a)
    lp = mycursor.fetchall()
    z = int(lp[0][0])

    amt = s + z

    total = "update Tickets set Total_amt=%s where T_no=%s"
    mycursor.execute(total, (amt, a))
    flights.commit()

    print("Seat bill:\tRs", s)
    print("Luggage bill:\tRs", z)
    print("\t-------")
    print("Total bill:\tRs", amt, "\n")


def info():
    a = input("Please enter your Ticket Number: ")

    sql = "select * from Tickets where T_no=%s"
    mycursor.execute(sql, a)
    rows = mycursor.fetchall()

    print("Ticket_no\tName\tDate\tDeparture\tArrival\tClass\tTicket_Amt\tLuggage_Amt\tTotal_Amt")
    print("---------------------------------------------------------------------")

    for i in rows:
        print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4], "\t", i[5], "\t", i[6], "\t", i[7], "\t", i[8])


def cancel():
    search = int(input("Enter ticket no.: "))
    state = "delete from Tickets where T_no=%s"
    mycursor.execute(state, search)
    flights.commit()
    print("Requested data has been deleted...")


def passengers():
    usrnm = input("Enter User Name: ")
    passwrd = input("Enter Password: ")

    if passwrd == "adminANA":
        print("Welcome", usrnm, "! You are viewing the entire passenger database of ANA Airlines!!")

        sql = "select * from Tickets"
        mycursor.execute(sql)
        rows = mycursor.fetchall()

        print("Ticket_no\tName\tDate\tDeparture\tArrival\tClass\tTicket_Amt\tLuggage_Amt\tTotal_Amt")
        print("---------------------------------------------------------------------")

        for i in rows:
            print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4], "\t", i[5], "\t", i[6], "\t", i[7], "\t", i[8])
    else:
        print("You are not cleared for viewing passenger info...")


x = input("Have you used this program before? (y or n): ")

if x == "n" or x == "N":
    setup()
else:
    flights = ps.connect(user='root', password='tiger', host='localhost', database='f2')
    mycursor = flights.cursor()
    print("Database Connected\n")
    mycursor.execute("use f2")
    print("Database used\n")

number = "select count(T_no) from Tickets"
mycursor.execute(number)
rows = mycursor.fetchall()
n = rows[0][0]
t = 11 * n

while True:
    print("""Welcome to ANA Airlines booking service!
Please proceed from number 1 to 5 to get your ticket
""")

    print("Enter 1 : To register a passenger")
    print("Enter 2 : To choose your seat class")
    print("Enter 3 : To get your luggage bill")
    print("Enter 4 : To get the complete bill")
    print("Enter 5 : To view your ticket information")
    print("Enter 6 : To cancel the ticket reservation")
    print("Enter 7 : To view all the passengers")
    print("Enter 8 : To exit the program\n")

    userinput = int(input("Enter your choice: "))

    if userinput == 1:
        t += 11
        register()
    elif userinput == 2:
        seatclass()
    elif userinput == 3:
        luggagebill()
    elif userinput == 4:
        ticketamount()
    elif userinput == 5:
        info()
    elif userinput == 6:
        cancel()
    elif userinput == 7:
        passengers()
    elif userinput == 8:
        break
    else:
        print("Please enter a valid option.")

flights.commit()
flights.close()
print("Thank you for flying with us! :)")git