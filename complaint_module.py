def register_complaint(complaints):
    name = input("write your name: ")
    room_no = int(input("write your room number: "))
    category = input("write your category: ")
    problem = input("write your problem: ")

    complaint = {
        "name": name,
        "room": room_no,
        "category": category,
        "problem": problem,
        "status": "pending"
    }

    complaints.append(complaint)
    print("complaint registered successfully")
