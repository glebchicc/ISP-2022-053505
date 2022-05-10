from setuptools import setup


setup(name="Serializer_to_JSON_YAML_TOML",
      version='1.0.0',
      description='This app has solutions to serialize and deserialize JSON, Yaml and Toml',
      author='glebchicc',
      url='https://github.com/glebchicc',
      requires=['TOML,YAML'],
      packages=['serializers,shell'],
      scripts=['shell/commands']
      )
