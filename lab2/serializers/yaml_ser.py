import yaml
from serializers.abstract_ser import Serializer
from serializers import packer


class YAMLSerializer(Serializer):

    def dumps(self, obj):
        return yaml.dump(packer.pack(obj))

    def loads(self, path):
        return packer.unpack(yaml.safe_load(path))
