class StudyParser(object):

    def parse_list_strategy(self,value):
        return value.split(";")

    def single_field_strategy(self, value):
        return value

    def parse_using_strategy(self, study, give_key, parse_strategy, value):
        study[give_key] = parse_strategy(value)

    def __init__(self):
        self.handlers = {}
        self.register('author', lambda study, val: self.parse_using_strategy(study, 'authors', self.parse_list_strategy, val))
        self.register('title', lambda study, val: self.parse_using_strategy(study, 'title', self.single_field_strategy, val))
        self.register('year', lambda study, val: self.parse_using_strategy(study, 'year', self.parse_list_strategy, val))

    def register(self, property, handler):
        self.handlers[property] = handler

    def parse_prop(self, study, key, value):
        key = key.replace("|", "").lower()

        handler = self.handlers.get(key)
        if (handler):
            handler(study, value)

    def parse_study(self,studyText):
        lines = studyText.split('\n')
        property_lines = filter(lambda line: line.startswith("|"), lines)

        properties = map(lambda line: line.split("="), property_lines)

        study = {}

        for prop in properties:
            key = prop[0]
            val = prop[1]
            self.parse_prop(study, key, val)

        return study
