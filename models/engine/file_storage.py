from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes the instance to JSON and
    deserializes JSON file to instance
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """
        Returns self.__object which is a dictionary
        """
        return self.__objects
    def new(self, obj):
        """
        sets in __objects the `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    def save(self):
        """
        serializes `__objects` to the JSON file in `__file_path`
        """
        dict_storage = {}
        for k, v in self.__objects.items():
            dict_storage[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dict_storage, f)
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
