import json
import os

VALID_ATTRIBUTES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

def get_level():
    while True:
        try:
            level = int(input("What level is the character currently?"))
            if level < 1:
                print("Level must be at least 1.")
                continue

            filename = f"level_{level}_character.json"
            if not os.path.isfile(filename):
                print(f"Could not find {filename}. Try a different level.")
                continue

            return level, filename
        except ValueError:
            print("Please enter a whole number.")


def get_attribute():
    print("Attributes:", ", ".join(VALID_ATTRIBUTES))
    while True:
        choice = input("Which attribute would you like to increase by 1? ").strip().lower()
        if choice not in VALID_ATTRIBUTES:
            return choice
        print("That is not a valid attribute. Please try again.")

def get_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please answer yes or no.")

def main():
    try:
        current_level, filename = get_level()
        with open(filename, "r") as file:
            character = json.load(file)
        character["level"] += 1
        character["armor_class"] += 1
        attribute = get_attribute()
        character["attributes"][attribute] += 1
        skill = input("Enter a new skill to add: ").strip()
    if skill:
        character["skills"].append(skill)
    if get_yes_no("Add a new weapon? (yes/no): "):
        weapon = input("Enter the weapon name: ").strip()
        if weapon:
            character["weapons"].append(weapon)

    new_level = character["level"]
    output_file = f"level_{new_level}_character.json"

    with open(output_file, "w") as file:
        json.dump(character, file, indent=4)

    print(f"Success! Character is now level {new_level} and saved to {output_file}")

except FileNotFoundError:
    print("Error: The character file could not be found.")

except json.JSONDecodeError:
    print("Error: The file is not valid JSON.")
except KeyError as e:
print(f"Error: Missing expected data in the character file ({e}).")
except Exception as e:
print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
