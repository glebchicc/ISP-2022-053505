from serializers import abstract_ser
from serializers import json_ser
from serializers import toml_ser
from serializers import yaml_ser


class SerializerCreator:

    def create_serializer(self) -> abstract_ser.Serializer:
        pass


class JSONSerializerCreator(SerializerCreator):

    def create_serializer(self) -> abstract_ser.Serializer:
        return json_ser.JSONSerializer()


class YAMLSerializerCreator(SerializerCreator):

    def create_serializer(self) -> abstract_ser.Serializer:
        return yaml_ser.YAMLSerializer()


class TOMLSerializerCreator(SerializerCreator):
    def create_serializer(self) -> abstract_ser.Serializer:
        return toml_ser.TOMLSerializer()
