---
title: Handy Commands for plasma py repo
menu:
  notes:
    name: Quick Helping commands
    identifier: notes-plasmapy-repo-cmd
    parent: notes-plasmapy
    weight: 30
---

{{< note title="Setup and debug">}}
```py
python3 -m pip install -e .[all] #Install changes-to be done from root dir
pytest # To run all test
pytest -k <Name> #Run a specific test
```
{{< /note>}}

{{< note title="Contribution tips!">}}
```md
1. Add Changelog entry per PR
2. Make sure a test is return for a feature
```
{{< /note>}}