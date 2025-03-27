# Basic method using **kwargs
def greet(**kwargs):
    if 'name' in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello, Guest!")

# Complex method using **kwargs


def describe_person(**kwargs):
    description = "Person details:\n"
    for key, value in kwargs.items():
        description += f"{key.capitalize()}: {value}\n"
    return description


# Example usage
greet(name="Andres")
print(describe_person(name="Andres", age=30,
      occupation="Developer", country="Spain"))
