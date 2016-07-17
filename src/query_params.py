

def parse_fields_param(request):
    """
    Takes a comma delimited list of fields, and returns a list of strings.
    e.g: field1, field2, field3 becomes ["field1", "field2", "field3"]
    """

    fields = request.args.get("fields")

    if not fields:
        return []
    else:
        return [field.strip() for field in fields.split(",")]


def parse_filter_param(request):
    """
    Takes a string of the foramt "key:val,key2:val2,key3:val3" and returns a
    list of key val tuples. e.g:
    [
        ("key" , "val")
        ("key2" , "val2"),
        ("key3" , "val3")
    ]
    """

    filter_param = request.args.get("filter")

    if not filter_param:
        return {}
    else:
        filter_pairs = filter_param.split(",?<!\\")
        filter_pairs = list(map(lambda pair: pair.replace("\\,", ","),
                                filter_pairs))

        return [(key, val) for (key, val)
                in map(lambda pair: pair.split(":"), filter_pairs)]
