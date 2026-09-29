def see_complaints(complaints):
    if len(complaints) == 0:
        print("No complaints registered.")
    else:
        print("            ALL COMPLAINTS")
        for complaint in complaints:
            print("Name:", complaint["name"])
            print("Room:", complaint["room"])
            print("Category:", complaint["category"])
            print("Problem:", complaint["problem"])
            print("Status:", complaint["status"])
            print()


def search_complaint(complaints):
    if len(complaints) == 0:
        print("No complaints registered.")
    else:
        room_no = int(input("Enter room number to search: "))
        found = False

        for complaint in complaints:
            if complaint["room"] == room_no:
                print("                 Complaint Found")
                print("Name:", complaint["name"])
                print("Room:", complaint["room"])
                print("Category:", complaint["category"])
                print("Problem:", complaint["problem"])
                print("Status:", complaint["status"])
                found = True

        if found == False:
            print("No complaint found for this room.")
