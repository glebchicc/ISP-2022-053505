from serializers.factory import *


def get_serializer(creator: SerializerCreator()):
    return creator.create_serializer()


def test_json_creator():
    serializer = get_serializer(JSONSerializerCreator())
    assert isinstance(serializer, json_ser.JSONSerializer)


def test_yaml_creator():
    serializer = get_serializer(YAMLSerializerCreator())
    assert isinstance(serializer, yaml_ser.YAMLSerializer)


def test_toml_creator():
    serializer = get_serializer(TOMLSerializerCreator())
    assert isinstance(serializer, toml_ser.TOMLSerializer)
