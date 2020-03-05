# Nested Dictionaries :

nested_dict = {"int": 123, "flout": 123.321, "list": [1, 2, 3], "nested": {"nested int": 100, "nested string": "inside nested"}}
print("\n\n********NESTED DICTIONARIES********")
print("int = " + nested_dict["int"].__str__())
print("flout = " + nested_dict["flout"].__str__())
print("list = " + nested_dict["list"].__str__())
print("nested dictionary = " + nested_dict["nested"].__str__())
print("[nested][nested int] = " + nested_dict["nested"]["nested int"].__str__())
print("[nested][nested string] = " + nested_dict["nested"]["nested string"].__str__())

nested_dict["nested"]["nested string"] = nested_dict["nested"]["nested string"].upper()
print("[nested][nested string].upper() = " + nested_dict["nested"]["nested string"].__str__())
