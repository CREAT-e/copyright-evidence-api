# copyright-evidence-api
A HTTP API to access the data hosted in the Copyright Evidence Wiki.

![TravisCI](https://travis-ci.org/CREAT-e/copyright-evidence-api.svg?branch=master)

## Quick Start

1. Create a configuration file.

```python
# See cfg/example.cfg for an example.
DEBUG = True
PORT = 3000
DATABASE = "/home/user/db/database.sqlite"
```

2. Set the environment variable `COPYRIGHT_EVIDENCE_API_CFG` to the path of your configuration file.

```shell
$ export COPYRIGHT_EVIDENCE_API_CFG=/home/user/copyright-evidence-api/cfg/development.cfg
```
3. Run the server.

```shell
$ git clone https://github.com/CREAT-e/copyright-evidence-api
$ cd copyright-evidence-api
$ python src/server.py
```

4. Open http://localhost:3000

## API Reference

### /studies GET

Returns a JSON list of studies.

```json
{
  "studies": [
    {
      "abstract": "...", 
      "authentic_link": "http://iisit.org/Vol7/IISITv7p321-328Acilar817.pdf", 
      "citation": "..."
      ...
    }, 
}
```