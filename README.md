# Create Site Hierarchy on the Cisco DNA Center via APIs

This is a Python sample code to showcase how to create the Site Hierarchy on the Cisco DNA Center via APIs. The Site Hierarchy is provided in JSON format and the sample code is then able to build this hierarchy on the Cisco DNA Center.

**Cisco Products & Services:**

- Cisco DNA Center

**Tools & Frameworks:**

- Python environment

**Usage**

- $ python create-site.py site-info.json

The above example will:
 - Retrieve the site details from the input file
 - Create this hierarchy on Cisco DNA Center

- Sample output

$ python create-site.py site-info.json

File Name site-info.json

EU-Demo Global
{"type": "area", "site": {"area": {"parentName": "Global", "name": "EU-Demo"}}}
{"status": "True", "siteId": "e02b7a4f-2c28-46cc-af70-dd01c58e2b78", "result": {"result": {"progress": "Site Creation completed successfully", "endTime": 1582680372583, "startTime": 1582680372546}}}
Area1 Global/EU-Demo
{"type": "area", "site": {"area": {"parentName": "Global/EU-Demo", "name": "Area1"}}}
{"status": "True", "siteId": "d1ba4af0-2bef-4512-8ca0-9607bf414329", "result": {"result": {"progress": "Site Creation completed successfully", "endTime": 1582680373549, "startTime": 1582680373440}}}
Area2 Global/EU-Demo
{"type": "area", "site": {"area": {"parentName": "Global/EU-Demo", "name": "Area2"}}}
{"status": "True", "siteId": "fd3c9ab9-39ba-4be7-ac87-bb084113c888", "result": {"result": {"progress": "Site Creation completed successfully", "endTime": 1582680374245, "startTime": 1582680374139}}}
Area3 Global/EU-Demo
{"type": "area", "site": {"area": {"parentName": "Global/EU-Demo", "name": "Area3"}}}
{"status": "True", "siteId": "acd786ce-e455-48ca-bd57-4adf9b8d520e", "result": {"result": {"progress": "Site Creation completed successfully", "endTime": 1582680374945, "startTime": 1582680374850}}}

-- Area Creation complete

Area1 Global/EU-Demo Area1-BLD1 170 West Tasman Drive, San Jose 95134
{"type": "building", "site": {"building": {"name": "Area1-BLD1", "address": "170 West Tasman Drive, San Jose 95134"}, "area": {"parentName": "Global/EU-Demo", "name": "Area1"}}}
{"status": "True", "siteId": "3f0c730e-aca5-4f9c-9d43-ba8f99ec3152", "result": {"result": {"progress": "Site Creation completed successfully", "endTime": 1582680376217, "startTime": 1582680376064}}}
Area1 Global/EU-Demo Area1-BLD2 171 West Tasman Drive, San Jose 95134
{"type": "building", "site": {"building": {"name": "Area1-BLD2", "address": "171 West Tasman Drive, San Jose 95134"}, "area": {"parentName": "Global/EU-Demo", "name": "Area1"}}}
{"status": "True", "siteId": "8679b2d5-d80f-4c00-9b65-6114e1005f9d", "result": {"result": {"progress": "Site Creation completed successfully", "endTime": 1582680377245, "startTime": 1582680377199}}}
Area2 Global/EU-Demo Area2-BLD1 180 West Tasman Drive, San Jose 95134
{"type": "building", "site": {"building": {"name": "Area2-BLD1", "address": "180 West Tasman Drive, San Jose 95134"}, "area": {"parentName": "Global/EU-Demo", "name": "Area2"}}}
{"status": "True", "siteId": "6ed2986f-4e76-495c-aa4a-1d150d31815e", "result": {"result": {"progress": "Site Creation completed successfully", "endTime": 1582680378152, "startTime": 1582680378048}}}
Area3 Global/EU-Demo Area3-BLD1 190 West Tasman Drive, San Jose 95134
{"type": "building", "site": {"building": {"name": "Area3-BLD1", "address": "190 West Tasman Drive, San Jose 95134"}, "area": {"parentName": "Global/EU-Demo", "name": "Area3"}}}
{"status": "True", "siteId": "9784656c-7e3a-4d1b-a932-0fff10ef0424", "result": {"result": {"progress": "Site Creation completed successfully", "endTime": 1582680379024, "startTime": 1582680378981}}}
Area3 Global/EU-Demo Area3-BLD2 191 West Tasman Drive, San Jose 95134
{"type": "building", "site": {"building": {"name": "Area3-BLD2", "address": "191 West Tasman Drive, San Jose 95134"}, "area": {"parentName": "Global/EU-Demo", "name": "Area3"}}}
{"status": "True", "siteId": "15f6ccfd-62b9-4105-87ee-1822d86b4a37", "result": {"result": {"progress": "Site Creation completed successfully", "endTime": 1582680379938, "startTime": 1582680379846}}}

-- Building Creation complete 

-- Site Creation complete


**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
