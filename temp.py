class Descriptor:
    def __get__(self, instance, owner):
        print(f"Getting the value from {instance}")
        return instance._value

    def __set__(self, instance, value):
        print(f"Setting the value to {value} in {instance}")
        instance._value = value

    def __delete__(self, instance):
        print(f"Deleting the value from {instance}")
        del instance._value

class MyClass:
    attribute = Descriptor()  # Descriptor instance

    def __init__(self, value):
        self._value = value  # Internal storage for the attribute

# Usage
obj = MyClass(10)
print(obj.attribute)  # Calls __get__
obj.attribute = 20    # Calls __set__
del obj.attribute     # Calls __delete__