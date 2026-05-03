# ================================
# Community Management System
# ================================

import json
import os
import re

DATA_FILE = "community_data.json"

def save_data():
    """Save members to file"""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(community_members, file)
    except:
        print("Error saving data!")

def load_data():
    """Load members from file"""
    global community_members
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                community_members = json.load(file)
        except:
            community_members = []

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_age(age):
    return age.isdigit() and 0 < int(age) < 120

# ================================
# UPDATE MEMBER FUNCTION
# ================================

def update_member():
    print("\n" + "=" * 40)
    print("  UPDATE MEMBER")
    print("=" * 40)

    member_id = input("Enter Member ID to update: ").strip()

    for member in community_members:
        if member['id'] == member_id:
            print(f"\nEditing {member['name']}")

            new_name = input("New Name (leave blank to keep): ")
            new_age = input("New Age (leave blank to keep): ")
            new_email = input("New Email (leave blank to keep): ")

            if new_name:
                member['name'] = new_name

            if new_age:
                if validate_age(new_age):
                    member['age'] = new_age
                else:
                    print("Invalid age!")

            if new_email:
                if validate_email(new_email):
                    member['email'] = new_email
                else:
                    print("Invalid email!")

            print("Member updated successfully!")
            save_data()
            return

    print("Member not found!")

# ================================
# STATISTICS FUNCTION
# ================================

def show_statistics():
    print("\n" + "=" * 40)
    print("  SYSTEM STATISTICS")
    print("=" * 40)

    total = len(community_members)

    if total == 0:
        print("No data available.")
        return

    total_age = sum(int(m['age']) for m in community_members if m['age'].isdigit())
    avg_age = total_age / total if total > 0 else 0

    print(f"Total Members: {total}")
    print(f"Average Age: {avg_age:.2f}")

# ================================
# EXPORT FUNCTION
# ================================

def export_to_txt():
    try:
        with open("members_export.txt", "w") as file:
            for m in community_members:
                file.write(f"{m['id']}, {m['name']}, {m['age']}, {m['email']}\n")
        print("Data exported successfully!")
    except:
        print("Export failed!")

# ================================
# EXTENDED MENU
# ================================

def extended_menu():
    print("\n" + "=" * 50)
    print("  EXTRA OPTIONS")
    print("=" * 50)
    print("  [6] Update Member")
    print("  [7] View Statistics")
    print("  [8] Export Data")
    print("=" * 50)

# ================================
# MODIFY MAIN LOOP (EXTEND ONLY)
# ================================

# ⚠️ Add this inside your main() loop WITHOUT removing existing ones

"""
elif choice == '6':
    update_member()
    input("Press ENTER to continue...")

elif choice == '7':
    show_statistics()
    input("Press ENTER to continue...")

elif choice == '8':
    export_to_txt()
    input("Press ENTER to continue...")
"""

# ================================
# AUTO LOAD DATA ON START
# ================================

load_data()
