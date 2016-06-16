class Study(object):
    """
    A model of all the metadata associated with a study on the wiki
    """

    def __init__(self, name=None, authors=None, title=None, year=None, full_citation=None, abstract=None,
                 definitive_link=None, open_acess_link=None, related_studies=None, main_results=None,
                 related_fundamental_issues=None, related_policies=None, disciplinary_classifications=None,
                 data_description=None, data_time_period=None, data_type=None, collection_methods=None, analysis_methods=None,
                 industries=None, countries=None, is_cross_country=None, is_comparative=None, is_gov_report=None, is_lit_review=None, funders=None):

                 self.name = name
                 self.authors = authors
                 self.title = title
                 self.year = year
