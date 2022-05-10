from serializers import packer
from serializers.abstract_ser import Serializer


class JSONSerializer(Serializer):

    def create_str(self, obj):
        if isinstance(obj, dict):
            strings = list()
            for key, value in obj.items():
                strings.append(f'{self.create_str(key)}:{self.create_str(value)},')
            return f"{{{''.join(strings)[:-1]}}}"
        elif isinstance(obj, str):
            s = obj.translate(str.maketrans({
                "\"": r"\"",
                "\\": r"\\",
            }))
            return f"\"{s}\""
        elif obj is None:
            return 'null'
        else:
            return str(obj)

    def dumps(self, obj):
        return self.create_str(packer.pack(obj))

    def loads(self, path):
        null = None
        return packer.unpack(eval(path))
