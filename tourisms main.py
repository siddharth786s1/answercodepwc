from tourism import Tourism
from invalid_place_exception import InvalidPlaceException

tourism = Tourism()
n = int(input("Enter the number of registrations:\n"))

for i in range(n):
    details = input(f"Enter the registration details {i+1}:\n").strip()
    try:
        passenger_name, place, no_of_days, no_of_tickets = details.split(":")
        validation = tourism.validate_place_name(place)
        if validation is not True:
            # validation returned the exception object; print its message
            print(validation.message)
            continue
        tourism.add_passenger_details(
            passenger_name,
            place,
            int(no_of_days),
            int(no_of_tickets)
        )
    except Exception:
        # Any parsing error or type conversion error; skip this record
        continue

search_place = input("Enter the Place that needs to be searched:\n")
validation = tourism.validate_place_name(search_place)
if validation is not True:
    print(validation.message)
else:
    matching_passengers = tourism.view_passenger_details(search_place)
    if not matching_passengers:
        print("No Passengers found")
    else:
        for passenger in matching_passengers:
            print(f"Passenger Name {passenger.get_passenger_name()}")
            print(f"Number Of Days {passenger.get_no_of_days()}")
            print(f"Number Of Tickets {passenger.get_no_of_tickets()}")
            print(f"Bill Amount {passenger.get_bill_amount()}")
