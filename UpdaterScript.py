import pymssql

#setting up connection
conn = pymssql.connect(
    host='stairway.usu.edu',
    user='s002_aeladunn',
    password='---------', #not actual
    database='s002_aeladunn')

cursor = conn.cursor()

ids = []

exit = 0
while(exit == 0):

    #Takes last name and validates it, then makes the query
    while(True):
        lname = input("Input a last name: ")
        if(len(lname)==0):
            print("Don't enter a blank")
        else:
            cursor.execute(f"""SELECT CustID, Lname, Fname, CustState, Marital
                            FROM Customer 
                            WHERE Lname LIKE '%{lname}%';""")

            for x in cursor:
                print(x)
            break

    while(True):
        custid = input("Enter the CustID of the record you'd like to change: ")
        try:
            custid = int(custid)
            cursor.execute(f"""SELECT *
                            FROM Customer 
                            WHERE CustID = {custid};""")
            for x in cursor: # only loops once here
                print(f"CustID: {x[0]}")
                print(f"Fname: {x[1]}")
                print(f"Lname: {x[2]}")
                print(f"Gender: {x[3]}")
                print(f"State: {x[4]}")
                print(f"HHI: {x[5]}")
                print(f"Marital: {x[6]}")
                print(f"Children: {x[7]}")
                print(f"Pets: {x[8]}")

            break
        except:
            print("Please enter a valid integer.")


    #Validating the field choice
    while(True):
        change = input("Whcih field of this record would you like to change?: ")
        change = change.upper()
        if change in("F", "L", "G", "S", "H", "M", "C", "P"):
            break
        else:
            print("Invalid. Please enter F, L, G, S, H, M, C, or P")


    #Validating the new value depending on the option chosen, then updating the database field with that value
    while(True):
        value = input(f"Write the value for the new field for {change}: ")
        if(change == "F" or change == "L"):
            if(len(value)==0 or len(value)>= 30):
                print("Must not be blank and must be less than 30 characters")
            else:
                if(change == "F"):
                    change = "Fname"
                else:
                    change = "Lname"
                break
        elif(change == "G"):
            value = value.lower()
            if(len(value) >= 2 or value not in("f","m","x","o")):
                print("Gender should be entered as f,m,x,o or left blank")
            else:
                change = "Gender"
                break
        elif(change == "S"):
            value = value.upper()
            if (len(value) != 2):
                print("Value needs to be two characters in length")
            else:
                change = "CustState"
                break
        elif(change == "H" or change == "C"):
            value = int(value)
            if(value < 0):
                print("Cannot enter a negative number. Try again")
            else:
                if(change == "H"):
                    change = "HHI"
                else:
                    change = "Children"
                break
        elif(change == "M"):
            value = value.lower()
            if(value not in ("single", "married", "")):
                print("Value needs to be married, single, or left blank")
            else:
                change = "Marital"
                break
        elif(change == "P"):
            value = value.lower()
            if(value not in("y", "n")):
                print("Value needs to be y or n")
            else:
                change = "HasPets"
                break

    cursor.execute(f"""UPDATE Customer
                            SET {change} = '{value}'
                            WHERE CustID = {custid};""")
    ids.append(custid)

    #commit here conn.commit()

    print("Here is the updated record:")
    print()
    cursor.execute(f"""SELECT *
                            FROM Customer 
                            WHERE CustID = {custid};""")
    for each in cursor:
        print(f"CustID: {each[0]}")
        print(f"Fname: {each[1]}")
        print(f"Lname: {each[2]}")
        print(f"Gender: {each[3]}")
        print(f"State: {each[4]}")
        print(f"HHI: {each[5]}")
        print(f"Marital: {each[6]}")
        print(f"Children: {each[7]}")
        print(f"Pets: {each[8]}")

    while(True):
        more = input("Would you like to update another record? (y or n)")
        more = more.lower()
        if(more == "n"):
            exit += 1
            break
        elif(more == "y"):
            break
        else:
            print("Enter y or n")


print()
print()
print("Number of updates completed is:", len(ids))
print("The updated Customer ID's are:", ids)
print("Session is now over")





