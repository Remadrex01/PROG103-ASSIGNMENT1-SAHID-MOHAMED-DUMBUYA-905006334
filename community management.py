"""
Community Data Processing System
A simple system to manage community member records.
Author: Rex AI
"""

# Global list to store community member records
# Each record will be a dictionary
community_members = []

def clear_screen():
    """Clears the terminal screen for a cleaner look."""
    print("\n" * 2)

def display_menu():
    """Displays the main menu options."""
    print("=" * 50)
    print("   COMMUNITY DATA PROCESSING SYSTEM")
    print("=" * 50)
    print("  [1] Add New Member")
    print("  [2] View All Members")
    print("  [3] Search Member")
    print("  [4] Delete Member")
    print("  [5] Exit")
    print("=" * 50)

def add_member():
    """Adds a new member to the system."""
    print("\n" + "=" * 40)
    print("  ADD NEW MEMBER - FILL IN THE FORM")
    print("=" * 40)
    try:
        # Show a clear "form" style input
        print("\n[FORM] Please fill in the following details:\n")

        member_id = input("  >>> MEMBER ID:     ")
        if not member_id.strip():
            print("\n  [!] ID cannot be empty!")
            return

        # Check if ID already exists
        for member in community_members:
            if member['id'] == member_id:
                print(f"\n  [!] Error: Member with ID '{member_id}' already exists.")
                return

        name = input("  >>> NAME:          ")
        if not name.strip():
            print("\n  [!] Name cannot be empty!")
            return

        age = input("  >>> AGE:           ")
        if not age.strip():
            print("\n  [!] Age cannot be empty!")
            return

        email = input("  >>> EMAIL:         ")
        if not email.strip():
            print("\n  [!] Email cannot be empty!")
            return

        # Create a dictionary for the new member
        new_member = {
            'id': member_id,
            'name': name,
            'age': age,
            'email': email
        }

        # Append to the global list
        community_members.append(new_member)

        print("\n" + "=" * 40)
        print("  [SUCCESS] Member added successfully!")
        print("=" * 40)
        print(f"\n  Name:    {name}")
        print(f"  ID:      {member_id}")
        print(f"  Age:     {age}")
        print(f"  Email:   {email}")
        print("\n  Press ENTER to continue...")
        input()

    except Exception as e:
        print(f"\n  [!] An error occurred: {e}")
        input("  Press ENTER to continue...")

def view_members():
    """Displays all members in the system."""
    print("\n" + "=" * 60)
    print("  VIEW ALL MEMBERS")
    print("=" * 60)

    if not community_members:
        print("\n  No records found. Add some members first!")
    else:
        print(f"\n  Total Members: {len(community_members)}\n")
        print("  " + "-" * 55)
        print(f"  {'ID':<10} {'NAME':<20} {'AGE':<5} {'EMAIL':<25}")
        print("  " + "-" * 55)

        # Iterate through the list and print each dictionary's values
        for member in community_members:
            print(f"  {member['id']:<10} {member['name']:<20} {member['age']:<5} {member['email']:<25}")
        print("  " + "-" * 55)

    print("\n  Press ENTER to continue...")
    input()

def search_member():
    """Searches for a member by ID or Name."""
    print("\n" + "=" * 40)
    print("  SEARCH MEMBER")
    print("=" * 40)

    search_term = input("\n  Enter Member ID or Name to search: ").strip()

    if not search_term:
        print("\n  [!] Search term cannot be empty!")
        return

    search_term = search_term.lower()
    found = False

    for member in community_members:
        if search_term == member['id'].lower() or search_term in member['name'].lower():
            if not found:
                print(f"\n  {'ID':<10} {'NAME':<20} {'AGE':<5} {'EMAIL':<25}")
                print("  " + "-" * 55)
                found = True
            print(f"  {member['id']:<10} {member['name']:<20} {member['age']:<5} {member['email']:<25}")

    if not found:
        print(f"\n  [!] No matching records found for '{search_term}'.")
    else:
        print("  " + "-" * 55)

    print("\n  Press ENTER to continue...")
    input()

def delete_member():
    """Deletes a member by ID."""
    print("\n" + "=" * 40)
    print("  DELETE MEMBER")
    print("=" * 40)

    # Show existing members first
    if not community_members:
        print("\n  No records to delete. Add some members first!")
        return

    print("\n  Current Members:")
    for member in community_members:
        print(f"    - {member['id']}: {member['name']}")

    member_id = input("\n  Enter Member ID to delete: ").strip()

    if not member_id:
        print("\n  [!] ID cannot be empty!")
        return

    global community_members
    initial_count = len(community_members)

    # Use list comprehension to filter out the member to be deleted
    community_members = [m for m in community_members if m['id'] != member_id]

    if len(community_members) < initial_count:
        print(f"\n  [SUCCESS] Member with ID '{member_id}' deleted successfully.")
    else:
        print(f"\n  [!] Member with ID '{member_id}' not found.")

    print("\n  Press ENTER to continue...")
    input()

def main():
    """Main function to run the system loop."""
    while True:
        clear_screen()
        display_menu()
        choice = input("\n  Enter your choice (1-5): ").strip()

        if choice == '1':
            add_member()
        elif choice == '2':
            view_members()
        elif choice == '3':
            search_member()
        elif choice == '4':
            delete_member()
        elif choice == '5':
            print("\n" + "=" * 40)
            print("  Exiting the system. Goodbye!")
            print("=" * 40)
            break
        else:
            print("\n  [!] Invalid choice. Please enter a number between 1 and 5.")
            input("  Press ENTER to try again...")

if __name__ == "__main__":
    main()
