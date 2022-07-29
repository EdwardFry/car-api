class DataStore:
    def __init__(self: object) -> None:
        self.id = 0
        self.storage_dict = {}

    def append(self: object, to_be_stored: int) -> None:
        self.storage_dict[self.id] = to_be_stored
        self.id += 1
    
    def delete(self: object, id_to_be_deleted: int) -> None:
        del self.storage_dict[id_to_be_deleted]
    
    def is_element_stored(self: object, id: int) -> bool:
        if id in self.storage_dict:
            return True
        return False

    def get_data(self: object) -> dict:
        return self.storage_dict


class Car:
    def __init__(self: object, make: str, model: str, build_date, colour_id: int) -> None:
        self.make = make
        self.model = model
        self.build_date = build_date
        self.colour_id = colour_id
