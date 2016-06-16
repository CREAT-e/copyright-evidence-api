class Study(object):

    """
    A model of all the metadata associated with a study on the wiki
    """
    def __init__(self, properties):

                 self.name = properties.get('name')
                 self.authors = properties.get('authors')
                 self.title = properties.get('title')
                 self.year = properties.get('year')
