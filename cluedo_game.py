"""
Cluedo / Clue - Project 2 Part 1
Author: King Solijonov

This is a text-based Python implementation of the Part 1 Cluedo game setup.
It includes:
- Mansion layout with rooms and room navigation
- Character definitions with starting positions
- Weapon definitions
- Random solution selection
- Player movement
- Suggestions involving a character, weapon, and room
"""

import random
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Character:
    name: str
    starting_room: str


class Mansion:
    """Represents the mansion map and room connections."""

    def __init__(self) -> None:
        self.rooms: Dict[str, List[str]] = {
            "Kitchen": ["Ballroom", "Dining Room"],
            "Ballroom": ["Kitchen", "Conservatory", "Hall"],
            "Conservatory": ["Ballroom", "Library"],
            "Dining Room": ["Kitchen", "Lounge"],
            "Lounge": ["Dining Room", "Hall"],
            "Hall": ["Lounge", "Ballroom", "Study"],
            "Study": ["Hall", "Library"],
            "Library": ["Study", "Conservatory", "Billiard Room"],
            "Billiard Room": ["Library"],
        }

    def get_rooms(self) -> List[str]:
        return list(self.rooms.keys())

    def get_connected_rooms(self, room: str) -> List[str]:
        return self.rooms.get(room, [])

    def is_valid_room(self, room: str) -> bool:
        return room in self.rooms

    def can_move(self, current_room: str, next_room: str) -> bool:
        return next_room in self.get_connected_rooms(current_room)


class CluedoGame:
    """Main game controller for Cluedo."""

    def __init__(self) -> None:
        self.mansion = Mansion()

        self.characters: List[Character] = [
            Character("Miss Scarlett", "Lounge"),
            Character("Colonel Mustard", "Dining Room"),
            Character("Mrs. White", "Kitchen"),
            Character("Mr. Green", "Conservatory"),
            Character("Mrs. Peacock", "Library"),
            Character("Professor Plum", "Study"),
        ]

        self.weapons: List[str] = [
            "Candlestick",
            "Revolver",
            "Rope",
            "Lead Pipe",
            "Knife",
            "Wrench",
        ]

        self.rooms: List[str] = self.mansion.get_rooms()

        self.solution: Tuple[str, str, str] = self.select_solution()

        self.player_character: Character | None = None
        self.current_room: str | None = None
        self.suggestions: List[Tuple[str, str, str]] = []

    def select_solution(self) -> Tuple[str, str, str]:
        """Randomly selects the murderer, weapon, and room."""
        murderer = random.choice(self.characters).name
        weapon = random.choice(self.weapons)
        room = random.choice(self.rooms)
        return murderer, weapon, room

    def display_intro(self) -> None:
        print("=" * 60)
        print("Welcome to Cluedo!")
        print("A murder has occurred in the mansion.")
        print("Your goal is to make suggestions and solve the mystery.")
        print("=" * 60)

    def display_mansion_layout(self) -> None:
        print("\nMansion Layout:")
        for room, connected_rooms in self.mansion.rooms.items():
            connections = ", ".join(connected_rooms)
            print(f"- {room} connects to: {connections}")

    def display_characters(self) -> None:
        print("\nCharacters:")
        for index, character in enumerate(self.characters, start=1):
            print(f"{index}. {character.name} - starts in {character.starting_room}")

    def display_weapons(self) -> None:
        print("\nWeapons:")
        for weapon in self.weapons:
            print(f"- {weapon}")

    def choose_character(self) -> None:
        self.display_characters()

        while True:
            try:
                choice = int(input("\nChoose your character by number: "))
                if 1 <= choice <= len(self.characters):
                    self.player_character = self.characters[choice - 1]
                    self.current_room = self.player_character.starting_room
                    print(
                        f"\nYou chose {self.player_character.name}. "
                        f"You start in the {self.current_room}."
                    )
                    return
                print("Invalid choice. Please choose a valid character number.")
            except ValueError:
                print("Please enter a number.")

    def show_current_location(self) -> None:
        print(f"\nCurrent Room: {self.current_room}")
        connected_rooms = self.mansion.get_connected_rooms(self.current_room)
        print("You can move to:")
        for index, room in enumerate(connected_rooms, start=1):
            print(f"{index}. {room}")

    def move_player(self) -> None:
        if self.current_room is None:
            print("No current room found.")
            return

        connected_rooms = self.mansion.get_connected_rooms(self.current_room)

        if not connected_rooms:
            print("There are no rooms connected to your current room.")
            return

        self.show_current_location()

        while True:
            try:
                choice = int(input("\nChoose a room to move to by number: "))
                if 1 <= choice <= len(connected_rooms):
                    next_room = connected_rooms[choice - 1]
                    self.current_room = next_room
                    print(f"\nYou moved to the {self.current_room}.")
                    return
                print("Invalid choice. Please select a listed room number.")
            except ValueError:
                print("Please enter a number.")

    def make_suggestion(self) -> None:
        if self.current_room is None:
            print("You must be in a room to make a suggestion.")
            return

        print("\nMake a Suggestion")
        print("A suggestion must include a character, a weapon, and your current room.")
        print(f"Current room for this suggestion: {self.current_room}")

        print("\nChoose a character:")
        for index, character in enumerate(self.characters, start=1):
            print(f"{index}. {character.name}")

        character_choice = self.get_number_choice(len(self.characters))
        suggested_character = self.characters[character_choice - 1].name

        print("\nChoose a weapon:")
        for index, weapon in enumerate(self.weapons, start=1):
            print(f"{index}. {weapon}")

        weapon_choice = self.get_number_choice(len(self.weapons))
        suggested_weapon = self.weapons[weapon_choice - 1]

        suggested_room = self.current_room
        suggestion = (suggested_character, suggested_weapon, suggested_room)
        self.suggestions.append(suggestion)

        print("\nYour suggestion:")
        print(
            f"I suggest it was {suggested_character}, "
            f"with the {suggested_weapon}, in the {suggested_room}."
        )

        self.check_suggestion(suggestion)

    def check_suggestion(self, suggestion: Tuple[str, str, str]) -> None:
        """Gives simple feedback for Part 1 without fully revealing the solution."""
        matches = 0
        for guess_item, solution_item in zip(suggestion, self.solution):
            if guess_item == solution_item:
                matches += 1

        print(f"\nClue Feedback: {matches} out of 3 parts match the hidden solution.")

        if matches == 3:
            print("Correct! You solved the murder mystery.")
        else:
            print("Keep investigating.")

    def show_previous_suggestions(self) -> None:
        if not self.suggestions:
            print("\nNo suggestions have been made yet.")
            return

        print("\nPrevious Suggestions:")
        for index, suggestion in enumerate(self.suggestions, start=1):
            character, weapon, room = suggestion
            print(f"{index}. {character} with the {weapon} in the {room}")

    def get_number_choice(self, max_choice: int) -> int:
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= max_choice:
                    return choice
                print(f"Invalid choice. Please enter a number from 1 to {max_choice}.")
            except ValueError:
                print("Please enter a number.")

    def game_menu(self) -> None:
        while True:
            print("\n" + "=" * 40)
            print("Game Menu")
            print("1. View current location")
            print("2. Move to another room")
            print("3. Make a suggestion")
            print("4. View previous suggestions")
            print("5. View mansion layout")
            print("6. View weapons")
            print("7. Quit game")
            print("=" * 40)

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.show_current_location()
            elif choice == "2":
                self.move_player()
            elif choice == "3":
                self.make_suggestion()
            elif choice == "4":
                self.show_previous_suggestions()
            elif choice == "5":
                self.display_mansion_layout()
            elif choice == "6":
                self.display_weapons()
            elif choice == "7":
                print("\nThanks for playing Cluedo!")
                break
            else:
                print("Invalid menu option. Please choose 1-7.")

    def start(self) -> None:
        self.display_intro()
        self.display_mansion_layout()
        self.display_weapons()
        self.choose_character()
        self.game_menu()


if __name__ == "__main__":
    game = CluedoGame()
    game.start()
