def parse_list(text, delim):
    return [i.strip() for i in filter(None, text.split(delim))]


def parse_scolon_list(text):
    return parse_list(text, ";")


def parse_comma_list(text):
    return parse_list(text, ",")


def parse_boolean(text):
    return text.lower() in ["y", "yes", "t", "true"]


study_enrichments = {
    "Abstract": {
        "name": "abstract"
    },
    "Authentic Link": {
        "name": "authentic_link"
    },
    "Author": {
        "name": "authors",
        "enrich": parse_scolon_list
    },
    "Comparative": {
        "name": "comparative",
        "enrich": parse_boolean
    },
    "Country": {
        "name": "country",
        "enrich": parse_scolon_list
    },
    "Cross-country": {
        "name": "cross_country",
        "enrich": parse_boolean
    },
    "Data": {
        "name": "data",
        "enrich": parse_comma_list
    },
    "Dataset": {
        "name": "dataset"
    },
    "Data Material Year": {
        "name": "data_material_year"
    },
    "Data Source": {
        "name": "data_source",
        "enrich": parse_scolon_list
    },
    "Data Type": {
        "name": "data_type"
    },
    "Data Year": {
        "name": "data_year"
    },
    "Description of Data": {
        "name": "data_description"
    },
    "Discipline": {
        "name": "discipline"
    },
    "EvidenceBasedPolicy": {
        "name": "evidence_based_policy"
    },
    "Evidence Based Policy": {
        "name": "evidence_based_policy"
    },
    "Full Citation": {
        "name": "full_citation"
    },
    "Fundamental Issue": {
        "name": "fundamental_issue"
    },
    "FundamentalIssue": {
        "name": "fundamental_issue"
    },
    "Funded By": {
        "name": "funded_by",
        "enrich": parse_scolon_list
    },
    "Government or policy": {
        "name": "government_or_policy",
        "enrich": parse_boolean
    },
    "Industry": {
        "name": "industry",
        "enrich": parse_scolon_list
    },
    "Intervention-Response": {
        "name": "intervention_response"
    },
    "Level of Aggregation": {
        "name": "aggregation_level"
    },
    "Link": {
        "name": "link"
    },
    "Literature review": {
        "name": "literature_review",
        "enrich": parse_boolean
    },
    "Method": {
        "name": "method",
        "enrich": parse_comma_list
    },
    "Method of Analysis": {
        "name": "analysis_method"
    },
    "Method of Collection": {
        "name": "collection_method"
    },
    "Name of Study": {
        "name": "name"
    },
    "Proposition": {
        "name": "proposition"
    },
    "PlainTextProposition": {
        "name": "proposition"
    },
    "Plain Text Proposition": {
        "name": "proposition"
    },
    "Reference": {
        "name": "references",
        "enrich": parse_scolon_list
    },
    "Sample Size": {
        "name": "sample_size"
    },
    "Title": {
        "name": "title"
    },
    "Year": {
        "name": "year"
    }
}
