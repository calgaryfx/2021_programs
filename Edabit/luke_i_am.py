# Luke Skywalker has family and friends. Help him remind them who is who. Given
# a string with a name, return the relation of that person to Luke.
def relation_to_luke(name):
    relation = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid",
        }

    return f"Luke, I am your {relation[name]}."

x = relation_to_luke("Darth Vader")
print(x)

x = relation_to_luke("Leia")
print(x)

x = relation_to_luke("Han")
print(x)

x = relation_to_luke("R2D2")
print(x)
