course_registry = {"CS101" : {"Instructor" : "Haynes", 
                              "Room Number" : 3004,
                              "Meeting Time": 8},
                    "CS102" : {"Instructor" : "Alvarado", 
                              "Room Number" : 3004,
                              "Meeting Time": 9},
                    "CS103" : {"Instructor" : "Rich", 
                              "Room Number" : 3004,
                              "Meeting Time": 10},
                    "NT110" : {"Instructor" : "Burke", 
                              "Room Number" : 3004,
                              "Meeting Time": 11},
                    "CM241" : {"Instructor" : "Lee", 
                              "Room Number" : 3004,
                              "Meeting Time": 12}
                              }

to_search = input("Enter what course you want to search: ").upper()                                   
if to_search in course_registry:
    print(course_registry[to_search])
else: 
    print("Enter Valid Course")