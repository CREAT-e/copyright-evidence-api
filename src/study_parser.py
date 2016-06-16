from study import Study

class StudyParser(object):

    def parse_list(self,value):
        return value.split(";")

    def parse_author(self, properties, value):
        properties['authors'] = self.parse_list(value)

    def parse_title(self, properties, value):
        properties['title'] = value

    def parse_year(self, properties, value):
        properties['year'] = value

    def __init__(self):
        self.handlers = {}
        self.register('author', self.parse_author)
        self.register('title', self.parse_title)
        self.register('year', self.parse_year)

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

        parsed_properties = {}

        for prop in properties:
            key = prop[0]
            val = prop[1]
            self.parse_prop(parsed_properties, key, val)

        return Study(parsed_properties)
