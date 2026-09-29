from complaint_module import register_complaint
from view_module import see_complaints, search_complaint
from manage_module import update_complaint, delete_complaint

complaints = []

while 1 < 2:
    print("                        HOSTEL COMPLAINT SYSTEM")
    print("1.register complaint")
    print("2.see complaint")
    print("3.search complaint")
    print("4.update complaint")
    print("5.delete complaint")
    print("6.exit")

    choices = int(input("enter what you want to do: "))

    if choices == 1:
        register_complaint(complaints)
    elif choices == 2:
        see_complaints(complaints)
    elif choices == 3:
        search_complaint(complaints)
    elif choices == 4:
        update_complaint(complaints)
    elif choices == 5:
        delete_complaint(complaints)
    elif choices == 6:
        print("Thank you for using Hostel Complaint System")
        break
    else:
        print("this option is not done yet ask SIR NUMAN to build more")
