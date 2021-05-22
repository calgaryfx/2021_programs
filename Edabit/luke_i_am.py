# Luke Skywalker has family and friends. Help him remind them who is who. Given
# a string with a name, return the relation of that person to Luke.
def relation_to_luke(name):
    relation = "Luke, I am your "

    if name == "Darth Vader":
        return (relation + "father.")
    elif name == "Leia":
        return (relation + "sister.")
    elif name == "Han":
        return (relation + "brother in law.")
    elif name == "R2D2":
        return (relation + "droid.")

x = relation_to_luke("Darth Vader")
print(x)

x = relation_to_luke("Leia")
print(x)

x = relation_to_luke("Han")
print(x)

x = relation_to_luke("R2D2")
print(x)
