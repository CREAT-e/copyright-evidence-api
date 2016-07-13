# copyright-evidence-api
A HTTP API to access the data hosted in the Copyright Evidence Wiki.

![TravisCI](https://travis-ci.org/CREAT-e/copyright-evidence-api.svg?branch=master)

## Quick Start

Create a configuration file:

```python
# See cfg/example.cfg for an example.
DEBUG = True
PORT = 3000
DATABASE = "/home/user/db/database.sqlite"
```

Set the environment variable `COPYRIGHT_EVIDENCE_API_CFG` to the path of your configuration file:

```shell
$ export COPYRIGHT_EVIDENCE_API_CFG=/home/user/copyright-evidence-api/cfg/development.cfg
```

Clone the repository:

```shell
$ git clone https://github.com/CREAT-e/copyright-evidence-api
$ cd copyright-evidence-api
```

Install the dependencies:

```shell
pip install -r requirements/development.txt
```

Run the server.

```shell
$ python src/server.py
```

Open <http://localhost:3000>

## API Reference

### /studies GET

Returns a JSON list of studies.

```
{
  "studies": [
    {
      "abstract": "...",
      "authentic_link": "http://iisit.org/Vol7/IISITv7p321-328Acilar817.pdf",
      "citation": "..."
      ...
    },
    ...
  ]
}
```

#### Query Parameters

#### ?fields=field1,field2

Returns only certain fields for each study.

* /studies/?fields=abstract, citation

```
{
  "studies": [
    {
      "abstract": "...",
      "citation": "..."
    },
    ...
  ]
}
```

#### ?filter=field1:value1,field2:value2

Returns only studies which have fields with the specified values. For list fields, one of the list values must match the given value

* /studies/filter=year:2007,funded_by:European%20Commission

```
{
  "studies": [
    {
      "abstract": "...",
      "citation": "...",
      "year":2007,
      "funded_by": ["European Commission", "ESPRC"]
      ...
    },
    ...
  ]
}
```

**Note**: Values with commas must be escaped with a leading backslash (e.g. /studies/filter=authors:Kauffman\,RJ,year:2007

### /values?field=field

Returns a list of all the legal values for a given field.

* /values/?field=year

```
{
  "values": [
    1980,
    1982
    ...
  ]
}
```

### /properties

Lists all the valid properties that can be retrieved for studies.

```
{
  "properties": [
  "cross_country",
  "funded_by",
  "literature_review",
   ...
   ]
  }
```
