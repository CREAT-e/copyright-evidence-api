class StudyParser(object):

    def strip_start_and_end(self,val):
        return val.lstrip().rstrip()

    def list_strategy(self,value):
        vals = value.split(";")
        return list(map(self.strip_start_and_end, vals))

    def single_field_strategy(self, value):
        return self.strip_start_and_end(value)

    def bullet_points_strategy(self, value):
        #print(value)
        bullets = value.split("*")
        points = list(map(self.strip_start_and_end, bullets))
        return points

    def parse_using_strategy(self, study, give_key, parse_strategy, value):
        study[give_key] = parse_strategy(value)

    def __init__(self):
        self.handlers = {}
        self.register('author', lambda study, val: self.parse_using_strategy(study, 'authors', self.list_strategy, val))
        self.register('title', lambda study, val: self.parse_using_strategy(study, 'title', self.single_field_strategy, val))
        self.register('year', lambda study, val: self.parse_using_strategy(study, 'year', self.single_field_strategy, val))
        self.register('full citation', lambda study, val: self.parse_using_strategy(study, 'citation', self.single_field_strategy, val))
        self.register('abstract', lambda study, val: self.parse_using_strategy(study, 'abstract', self.single_field_strategy, val))
        self.register('link', lambda study, val: self.parse_using_strategy(study, 'link', self.single_field_strategy, val))
        self.register('authentic link', lambda study, val: self.parse_using_strategy(study, 'open_access_link', self.single_field_strategy, val))
        self.register('reference', lambda study, val: self.parse_using_strategy(study, 'reference', self.single_field_strategy, val))
        self.register('plain text proposition', lambda study, val: self.parse_using_strategy(study, 'study_findings', self.bullet_points_strategy, val))

        # TODO: These two need a different parser from the 'list_strategy' parser... (A. <value>, B.value)
        self.register('fundamentalissue',lambda study, val: self.parse_using_strategy(study, 'relevant_issues', self.list_strategy, val))
        self.register('evidencebasedpolicy',lambda study, val: self.parse_using_strategy(study, 'relevant_issues', self.list_strategy, val))

    def register(self, property, handler):
        self.handlers[property] = handler

    def parse_prop(self, study, key, value):
        key = key.replace("|", "").lower()

        handler = self.handlers.get(key)
        if (handler):
            handler(study, value)

    def parse_study(self,studyText):
        lines = studyText.split('|')
        lines = map(lambda line: line.replace("{{", "").replace("}}", "").rstrip(), lines)
        lines = filter(lambda line: "=" in line, lines)

        properties = map(lambda line: line.split("=", 1), lines)

        study = {}
        for prop in properties:
            key = prop[0]
            val = prop[1]
            self.parse_prop(study, key, val)

        return study
