athlete_data = []
event_data = {}
medal_count = {}

def add_details():
    global athlete_data, event_data, medal_count
    
    athlete_name = input("Enter athlete name: ")
    athlete_country = input("Enter athlete country: ")
    event_name = input("Enter event name: ")
    medal_type = input("Enter medal type (Gold/Silver/Bronze): ")

    if medal_type not in ["Gold", "Silver", "Bronze"]:
        print("Invalid medal type. Please enter Gold, Silver, or Bronze.")
        return

    
    athlete_data.append({
        'name': athlete_name,
        'country': athlete_country,
        'event': event_name,
        'medal': medal_type
    })

    
    if event_name not in event_data:
        event_data[event_name] = []

    event_data[event_name].append({
        'name': athlete_name,
        'country': athlete_country,
        'medal': medal_type
    })

    
    if athlete_country not in medal_count:
        medal_count[athlete_country] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
    
    medal_count[athlete_country][medal_type] += 1

    print(f"Details added for athlete {athlete_name}.")

def view_details():
    event_name = input("Enter event name to view details: ")
    
    if event_name not in event_data:
        print("Event not found.")
        return
    
    print(f"Details for event: {event_name}")
    for record in event_data[event_name]:
        print(f"Athlete: {record['name']}, Country: {record['country']}, Medal: {record['medal']}")

def view_medal_count_by_country():
    if not medal_count:
        print("No medals available.")
        return
    
    print("Medal Count by Country:")
    for country, medals in medal_count.items():
        print(f"{country}: Gold: {medals['Gold']}, Silver: {medals['Silver']}, Bronze: {medals['Bronze']}")
        
def search_athlete_performance():
    athlete_name = input("Enter athlete name to search performance: ")
    results = [record for record in athlete_data if record['name'].lower() == athlete_name.lower()]
    
    if not results:
        print("No records found for this athlete.")
        return
    
    print(f"Performance details for athlete: {athlete_name}")
    for record in results:
        print(f"Event: {record['event']}, Country: {record['country']}, Medal: {record['medal']}")



def view_event_details():
    event_name = input("Enter event name to view details: ")
    
    if event_name not in event_data:
        print("Event not found.")
        return
    
    print(f"Details for event: {event_name}")
    for record in event_data[event_name]:
        print(f"Athlete: {record['name']}, Country: {record['country']}, Medal: {record['medal']}")

def main_menu():
    while True:
        print("\nOlympic Records Menu")
        print("1. Add Details")
        print("2. View Details")
        print("3. View Medal Count by Country")
        print("4. Search Athlete Performance")
        print("5. View Event Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_details()
        elif choice == '2':
            view_details()
        elif choice == '3':
            view_medal_count_by_country()
        elif choice == '4':
            search_athlete_performance()
        elif choice == '5':
            view_event_details()
        elif choice == '6':
            print("Exiting")
            break  
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
