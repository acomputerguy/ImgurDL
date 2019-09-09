import yaml

class ReadYaml():
    yamldict = {}

    def __init__(self, givenKey):
        yaml_streamr = open('config/setup.yaml', 'r')
        conf = yaml.safe_load(yaml_streamr)
        for key, value in conf.items():
            if (givenKey == key):
                self.yamldict = conf[givenKey]
        del yaml_streamr
