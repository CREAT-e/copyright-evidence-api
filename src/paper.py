

class Paper:
    """
    A model of a paper in the copyright evidence wiki
    """

    def __init__(self, metadata):
       """
       metadata: A dictionary containing the metadata available about the paper (year, authors, title, etc).
                 Each dictionary has a 'key' of the metadata property (e.g. 'year, 'authors', etc) and a
                 value that is either a string if there is one value, or a list of strings if there are many.
                 e.g.
                 {
                    "title" : "Digital Music Consumption on the Internet: Evidence from Clickstream Data",
                    "year" : 2013,
                    "authors" : ["Agular, L", "Martens, B."]
                    ...
                 }

       """
