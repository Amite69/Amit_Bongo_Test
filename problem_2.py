class Person(object):

    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def print_depth(data, depth=1):
    # check
    if isinstance(data, dict):
        for key in data:
            print(f"{key} {depth}")
            if isinstance(data[key], object):
                print_depth(data[key], depth + 1)
    elif isinstance(data, Person):
        person_fields = ["first_name", "last_name", "father"]
        for field in person_fields:
            print(f"{field} {depth}")
        if isinstance(data.father, Person):
            print_depth(data.father, depth + 1)


def main():
    person_a = Person("User", "1", None)
    person_b = Person("User", "2", person_a)
    print_depth({
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b}
        }
    })


if __name__ == "__main__":
    main()
