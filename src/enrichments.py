import re
import string


def parse_list(text, delim):
    return [i.strip() for i in filter(None, text.split(delim))]


def parse_scolon_list(text):
    return parse_list(text, ";")


def parse_comma_list(text):
    return parse_list(text, ",")


def parse_boolean(text):
    return text.lower() in ["y", "yes", "t", "true"]


def strip_trailing_punctuation(text):
    return text.strip(string.punctuation)


def parse_policy(text):
    policies = [strip_trailing_punctuation(policy).partition("(")[0]
                for policy in re.split("[,]*\s*[A-Z][.]\s", text)]
    policies.pop(0)
    return policies


def parse_fundamental_issue(text):
    issues = [issue.strip(string.punctuation)
              for issue in re.split("[,]*\s*[1-9][.]\s", text)]
    issues.pop(0)
    return issues


study_enrichments = {
    "Abstract": {
        "name": "abstract"
    },
    "Authentic Link": {
        "name": "authentic_link"
    },
    "Author": {
        "name": "authors",
        "enrich": parse_scolon_list,
        "aggregatable": True
    },
    "Comparative": {
        "name": "comparative",
        "enrich": parse_boolean,
        "aggregatable": True
    },
    "Country": {
        "name": "country",
        "enrich": parse_scolon_list,
        "aggregatable": True
    },
    "Cross-country": {
        "name": "cross_country",
        "enrich": parse_boolean,
        "aggregatable": True
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
        "enrich": parse_scolon_list,
        "aggregatable": True
    },
    "Data Type": {
        "name": "data_type",
        "aggregatable": True
    },
    "Data Year": {
        "name": "data_year",
        "aggregatable": True
    },
    "Description of Data": {
        "name": "data_description"
    },
    "Discipline": {
        "name": "discipline"
    },
    "EvidenceBasedPolicy": {
        "name": "evidence_based_policy",
        "enrich": parse_policy,
        "aggregatable": True
    },
    "Evidence Based Policy": {
        "name": "evidence_based_policy",
        "enrich": parse_policy,
        "aggregatable": True
    },
    "Full Citation": {
        "name": "full_citation"
    },
    "Fundamental Issue": {
        "name": "fundamental_issue",
        "enrich": parse_fundamental_issue,
        "aggregatable": True
    },
    "FundamentalIssue": {
        "name": "fundamental_issue",
        "enrich": parse_fundamental_issue,
        "aggregatable": True
    },
    "Funded By": {
        "name": "funded_by",
        "enrich": parse_scolon_list,
        "aggregatable": True
    },
    "Government or policy": {
        "name": "government_or_policy",
        "enrich": parse_boolean,
        "aggregatable": True
    },
    "Industry": {
        "name": "industry",
        "enrich": parse_scolon_list,
        "aggregatable": True
    },
    "Intervention-Response": {
        "name": "intervention_response"
    },
    "Level of Aggregation": {
        "name": "aggregation_level",
        "enrich": strip_trailing_punctuation,
        "aggregatable": True
    },
    "Link": {
        "name": "link"
    },
    "Literature review": {
        "name": "literature_review",
        "enrich": parse_boolean,
        "aggregatable": True
    },
    "Method": {
        "name": "method",
        "enrich": parse_comma_list,
        "aggregatable": True
    },
    "Method of Analysis": {
        "name": "analysis_method",
        "enrich": parse_comma_list
    },
    "Method of Collection": {
        "name": "collection_method",
        "enrich": parse_comma_list
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
        "enrich": parse_scolon_list,
        "aggregatable": True
    },
    "Sample Size": {
        "name": "sample_size",
        "aggregatable": True
    },
    "Title": {
        "name": "title"
    },
    "Year": {
        "name": "year",
        "aggregatable": True
    }
}
