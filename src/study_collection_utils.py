def filter_studies(studies, fields_filter):
    if not fields_filter:
        return studies

    return [study for study in studies if matches_filter(study, fields_filter)]


def matches_filter(study, fields_filter):
    matching = [key in study and study[key] == val
                for (key, val) in fields_filter]
    return all(matching)


def deleted_unrequired_fields(studies, fields):
    if not fields:
        return studies

    for study in studies:
        delete_unwanted_fields(study, fields)

    # Remove any studies that are empty because they did not have the requested
    # field
    return filter(any, studies)


def delete_unwanted_fields(study, fields):
    unwanted_fields = set(study) - set(fields)

    for unwanted_field in unwanted_fields:
        del study[unwanted_field]
