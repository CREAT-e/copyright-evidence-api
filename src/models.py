from enrichments import study_enrichments


class Study(object):

    def __init__(self, wikitext):
        self._init_from_wikitext(wikitext)

    def _init_from_wikitext(self, wikitext):
        lines = wikitext.split("|")
        lines = filter(lambda l: "=" in l, lines)
        lines = filter(lambda l: "={{" not in l, lines)
        lines = map(lambda l: l.rstrip("\n}}"), lines)
        for line in lines:
            key, val = line.split("=", 1)
            setattr(self, key, val)

    def enriched_json(self):
        json = self.__dict__
        for enrichment in study_enrichments:
            if enrichment not in json:
                continue
            name = study_enrichments[enrichment].get("name")
            enrich = study_enrichments[enrichment].get("enrich")
            val = json[enrichment]
            del json[enrichment]
            if val:
                json[name] = enrich(val) if enrich else val
        return json

    @staticmethod
    def valid_fields(aggregatable_only):
        fields = [enrichment["name"]
                  for enrichment in study_enrichments.values()
                  if not aggregatable_only or enrichment.get("aggregatable")]
        return list(set(fields))
