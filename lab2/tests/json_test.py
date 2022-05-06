import math
import os

from ser_entities import class_obj, functions

from serializers import json_ser


def test_dump_load_function():
    serializer = json_ser.JSONSerializer()
    file = open("output.json", "w")
    serializer.dump(functions.f, file.name)
    func = serializer.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert math.sin(42 * 123 * 1) == func(1)


def test_dump_load_function2():
    serializer = json_ser.JSONSerializer()
    file = open("output.json", "w")
    serializer.dump(functions.div_of_two, file.name)
    func = serializer.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert 5 - 2 == func(5, 2)


def test_dump_load_object():
    serializer = json_ser.JSONSerializer()
    file = open("output.json", "w")
    serializer.dump(class_obj.student_object, file.name)
    obj = serializer.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert obj.name == "Kirill"
