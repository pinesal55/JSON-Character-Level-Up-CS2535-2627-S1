import json
def main():
    with open("level_1.json", "r") as file:
        character = json.load(file)
    character["level"] += 1
    character["armor_class"] += 1
    character["attributes"]["strength"] += 2
    character["attributes"]["constitution"] += 1
    character["skills"].append("Survival")
    character["weapons"].append("Silver Dagger")

    with open("level_2.json", "w") as file:
        json.dump(character, file, indent=4)
    print("Level up complete! Saved to level_2_character.json")
if __name__ == "__main__":
    main()