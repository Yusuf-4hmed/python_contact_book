from pathlib import Path
import json


contacts = [
    # {"name": "Peter Parker",
    #  "phone": "(300) 2342-2412",
    #  "email": "peterparker616@dailybugle.net",
    #  }
]

def saveData():
    contacts_data_write = open("contacts_data.json", "w")
    json.dump(contacts, contacts_data_write)
    contacts_data_write.close()
def loadData():
    contacts_data_load = open("contacts_data.json", "r" )
    global contacts
    contacts = json.load(contacts_data_load)
    contacts_data_load.close()


# print(contacts[0])

# print(contacts[-1]["name"])

datapath = Path("contacts_data.json")

if datapath.exists():
    loadData()
else:
    open("contacts_data.json", "x")

while True:
    

    user_choice = input("1. Add Contact  2. View Contact/s  3. Delete Contact 4. Exit")

    if user_choice == "1":
        contact_name_input = input("What is the name of your contact?")
        contact_phone_input = input("What is the phone no of your contact?")
        contact_email_input = input("What is the email of your contact?")
        contacts.append({"name": f"{contact_name_input}"})
        contacts[-1]["phone"] = f"{contact_phone_input}"
        contacts[-1]["email"] = f"{contact_email_input}"
        print("Contact added!")
        # print(contacts)
        saveData()
    elif user_choice == "2":
        
        for contact in contacts:
            print(f"name: {contact["name"]}")
            print(f"phone: {contact["phone"]}")
            print(f"email: {contact["email"]}")
            print("\n")
        print("Contact/s loaded!")
    elif user_choice == "3":
        contact_delete_name = input("What is the full name of the contact you want to delete?")
        contact_delete_match = False
        
        for contact in contacts:
            if contact["name"] == contact_delete_name:
                contact_delete_match = True
                # print(f"{contacts.index(contact)}")
                contacts.pop(contacts.index(contact))
                saveData()
                break

        if contact_delete_match == True:
            print("Found match!")
            print("Deleted contact!")
        elif contact_delete_match == False:
            print("No match found.")

       
            
    elif user_choice == "4":
        saveData()
        print("Goodbye!")
        break
            

# for contact in contacts:
#     print(f"name: {contact["name"]}")
#     print(f"phone: {contact["phone"]}")
#     print(f"email: {contact["email"]}")
#     print("\n")

