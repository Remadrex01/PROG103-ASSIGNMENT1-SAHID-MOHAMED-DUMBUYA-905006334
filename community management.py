""" Community Data Processing System
A simple system to manage community member records.
"""

import re

# Global list to store community member records
# Each record will be a dictionary
community_members = []


def sanitize_input(value: str) -> str:
    """Sanitize and normalize user input."""
    return value.strip()


def validate_email(email: str) -> bool:
    """Validate email format using a simple regex."""
    return bool(re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email))


def validate_age(age: str) -> bool:
    """Validate that age is a positive integer between 1 and 120."""
    return age.isdigit() and 1 <= int(age) <= 120


def clear_screen():
    """Clears the terminal screen for a cleaner look."""
    print("\n" * 2)


def pause(wait: bool = True, message: str = "  Press ENTER to continue..."):
    """Pause to allow the user to read output during interactive use."""
    if wait:
        input(message)


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


def add_member(pause: bool = True):
    """Adds a new member to the system."""
    print("\n" + "=" * 40)
    print("  ADD NEW MEMBER - FILL IN THE FORM")
    print("=" * 40)

    try:
        print("\n[FORM] Please fill in the following details:\n")

        member_id = sanitize_input(input("  >>> MEMBER ID:     "))
        if not member_id:
            print("\n  [!] ID cannot be empty!")
            return

        # Check if ID already exists
        for member in community_members:
            if member['id'].lower() == member_id.lower():
                print(f"\n  [!] Error: Member with ID '{member_id}' already exists.")
                return

        name = sanitize_input(input("  >>> NAME:          "))
        if not name:
            print("\n  [!] Name cannot be empty!")
            return

        # ✅ Improved AGE validation (loop)
        while True:
            age = sanitize_input(input("  >>> AGE:           "))
            if not age:
                print("\n  [!] Age cannot be empty!")
                continue
            if not validate_age(age):
                print("\n  [!] Age must be a number between 1 and 120.")
                continue
            break

        # ✅ Improved EMAIL validation (loop)
        while True:
            email = sanitize_input(input("  >>> EMAIL:         "))
            if not email:
                print("\n  [!] Email cannot be empty!")
                continue
            if not validate_email(email):
                print("\n  [!] Invalid email format.")
                continue
            break

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

        pause(pause)

    except Exception as e:
        print(f"\n  [!] An error occurred: {e}")
        pause(pause)


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
    global community_members  # ✅ FIXED LINE

    print("\n" + "=" * 40)
    print("  DELETE MEMBER")
    print("=" * 40)

    if not community_members:
        print("\n  No records to delete. Add some members first!")
        return

    print("\n  Current Members:")
    for member in community_members:
        print(f"    - {member['id']}: {member['name']}")

    member_id = sanitize_input(input("\n  Enter Member ID to delete: "))

    if not member_id:
        print("\n  [!] ID cannot be empty!")
        return

    initial_count = len(community_members)

    community_members = [m for m in community_members if m['id'].lower() != member_id.lower()]

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
