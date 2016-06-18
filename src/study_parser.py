class StudyParser(object):

    def strip_start_and_end(self, val):
        return val.lstrip().rstrip()

    def list_strategy(self, value):
        vals = value.split(";")
        return list(map(self.strip_start_and_end, vals))

    def single_field_strategy(self, value):
        return self.strip_start_and_end(value)

    def bullet_points_strategy(self, value):
        bullets = value.split("*")
        points = list(map(self.strip_start_and_end, bullets))
        return points

    def parse(self, study, give_key, parse_strategy, value):
        study[give_key] = parse_strategy(value)

    def __init__(self):
        self.handlers = {
            "author": lambda s, v:
                self.parse(s, "authors", self.list_strategy, v),
            "title": lambda s, v:
                self.parse(s, "title", self.single_field_strategy, v),
            "year": lambda s, v:
                self.parse(s, "year", self.single_field_strategy, v),
            "full citation": lambda s, v:
                self.parse(s, "citation", self.single_field_strategy, v),
            "abstract": lambda s, v:
                self.parse(s, "abstract", self.single_field_strategy, v),
            "link": lambda s, v:
                self.parse(s, "link", self.single_field_strategy, v),
            "authentic link": lambda s, v:
                self.parse(s, "authentic_link", self.single_field_strategy, v),
            "reference": lambda s, v:
                self.parse(s, "reference", self.single_field_strategy, v),
            "plain text proposition": lambda s, v:
                self.parse(s, "findings", self.bullet_points_strategy, v),
            "fundamentalissue": lambda s, v:
                self.parse(s, "relevant_issues", self.list_strategy, v),
            "evidencebasedpolicy": lambda s, v:
                self.parse(s, "evidence_policies", self.list_strategy, v)
        }

    def parse_prop(self, study, key, value):
        key = key.replace("|", "").lower()

        handler = self.handlers.get(key)
        if (handler):
            handler(study, value)

    def parse_study(self, studyText):
        lines = studyText.split("|")
        lines = map(lambda l: l.replace("{{", "").replace("}}", ""), lines)
        lines = map(lambda l: l.rstrip(), lines)
        lines = filter(lambda l: "=" in l, lines)

        properties = map(lambda line: line.split("=", 1), lines)

        study = {}
        for prop in properties:
            key = prop[0]
            val = prop[1]
            self.parse_prop(study, key, val)

        return study
