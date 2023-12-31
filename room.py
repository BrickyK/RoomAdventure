#room.py

class Room:

    def __init__(self, name: str, image_filepath: str):
        """
            A Room in the Room Adventure game

            name: str - a name for the room
            image_filepath: str - the relative filepath to the image
                ex: images/room1.gif
        """
        self.name = name
        self.image_filepath = image_filepath
        self.exits = {}
        self.items = {}
        self.grabbables = []

    #additional methods
    def add_exit(self, location: str, room: 'Room | None'):
        """
            Adds an exit to the room.

            location: str - a direction that identifies the location of the room you will go to
            room: Room | None - a room object or none that the location leads to
                In the case of a death sequence, use None instead of a Room object.
        """
        self.exits[location] = room

    def add_item(self, label: str, description: str) -> None:
        self.items:[label] = description
        

    def add_grabbable(self, item: str):
        self.grabbables.append(item)

    def delete_grabbable(self, item: str):
        self.grabbables.remove(item)

    def __str__(self) -> str:
        result = f"you are in {self.name}"
        result += "you see: "
        for item in self.items.keys():
            result += item + " "
        result += "\n"

        result += "exits: "
        for exit in self.exits.keys():
            result += exit + " "
        result += "\n"


        return result
