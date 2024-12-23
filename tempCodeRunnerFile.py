
            blood_type = input("Enter blood type to search: ")
            donors = find_donors(blood_type)
            if donors:
                print("Donors with blood type", blood_type)
                for donor in donors: