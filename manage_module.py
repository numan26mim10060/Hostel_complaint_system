def update_complaint(complaints):
    if len(complaints) == 0:
        print("No complaints registered.")
    else:
        room_no = int(input("Enter room number to update: "))
        found = False

        for complaint in complaints:
            if complaint["room"] == room_no:
                print("Current status:", complaint["status"])
                new_status = input("Enter new status (pending/resolved): ")
                complaint["status"] = new_status
                print("Complaint updated successfully!")
                found = True

        if found == False:
            print("No complaint found for this room.")


def delete_complaint(complaints):
    if len(complaints) == 0:
        print("No complaints registered.")
    else:
        room_no = int(input("Enter room number to delete: "))
        found = False

        for complaint in complaints:
            if complaint["room"] == room_no:
                complaints.remove(complaint)
                print("Complaint deleted successfully!")
                found = True
                break

        if found == False:
            print("No complaint found for this room.")
