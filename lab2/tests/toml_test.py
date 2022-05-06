import math
import os

from ser_entities import class_obj, functions

from serializers import toml_ser


def test_dump_load_object():
    serializer = toml_ser.TOMLSerializer()
    file = open("output.toml", "w")
    serializer.dump(class_obj.student_object, file.name)
    obj = serializer.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert obj.avg_score == 8.0


def test_dump_load_object2():
    serializer = toml_ser.TOMLSerializer()
    file = open("output.toml", "w")
    serializer.dump(class_obj.student_object, file.name)
    obj = serializer.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert obj.name == 'Kirill'


def test_dump_load_function():
    serializer = toml_ser.TOMLSerializer()
    file = open("output.toml", "w")
    serializer.dump(functions.div_of_two, file.name)
    func = serializer.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert 5 - 2 == func(5, 2)
