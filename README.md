# Create Site Hierarchy on the Cisco DNA Center via APIs

This is a Python sample code to showcase how to create the Site Hierarchy on the Cisco DNA Center via APIs. The Site Hierarchy is provided in JSON format and the sample code is then able to build this hierarchy on the Cisco DNA Center.

**Cisco Products & Services:**

- Cisco DNA Center

**Tools & Frameworks:**

- Python environment

**Usage**

- $ python3 create-site.py site-info.json

The above example will:
 - Retrieve the site details from the input file
 - Create this hierarchy on Cisco DNA Center

- Sample output

$ python3 create-site.py site-info.json

File Name site-info.json

EU-Demo Global
{"type": "area", "site": {"area": {"name": "EU-Demo", "parentName": "Global"}}}
{"result": {"result": {"startTime": 1582780979809, "endTime": 1582780980716, "progress": "Site Creation completed successfully"}}, "status": "True", "siteId": "99afe126-07d9-41d2-a4ce-d3de141c0f56"}
Area1 Global/EU-Demo
{"type": "area", "site": {"area": {"name": "Area1", "parentName": "Global/EU-Demo"}}}
{"result": {"result": {"startTime": 1582780982306, "endTime": 1582780982430, "progress": "Site Creation completed successfully"}}, "status": "True", "siteId": "f9642956-7ab2-4261-8a9c-dc106deff46f"}
Area2 Global/EU-Demo
{"type": "area", "site": {"area": {"name": "Area2", "parentName": "Global/EU-Demo"}}}
{"result": {"result": {"startTime": 1582780983902, "endTime": 1582780984104, "progress": "Site Creation completed successfully"}}, "status": "True", "siteId": "88d5521f-47d7-4f39-a969-5f39d13f5946"}
Area3 Global/EU-Demo
{"type": "area", "site": {"area": {"name": "Area3", "parentName": "Global/EU-Demo"}}}
{"result": {"result": {"startTime": 1582780985510, "endTime": 1582780985625, "progress": "Site Creation completed successfully"}}, "status": "True", "siteId": "44622f14-1c69-450b-ae45-cf91ee25267a"}

-- Area Creation complete

Area1 Global/EU-Demo Area1-BLD1 170 West Tasman Drive, San Jose 95134
{"type": "building", "site": {"area": {"name": "Area1", "parentName": "Global/EU-Demo"}, "building": {"name": "Area1-BLD1", "address": "170 West Tasman Drive, San Jose 95134"}}}
{"result": {"result": {"startTime": 1582780987583, "endTime": 1582780987624, "progress": "Site Creation completed successfully"}}, "status": "True", "siteId": "69b9e343-cc4b-44c4-a5f8-55b6c2480300"}
Area1 Global/EU-Demo Area1-BLD2 171 West Tasman Drive, San Jose 95134
{"type": "building", "site": {"area": {"name": "Area1", "parentName": "Global/EU-Demo"}, "building": {"name": "Area1-BLD2", "address": "171 West Tasman Drive, San Jose 95134"}}}
{"result": {"result": {"startTime": 1582780989035, "endTime": 1582780989068, "progress": "Site Creation completed successfully"}}, "status": "True", "siteId": "2950430e-050a-4919-a4f4-c8e822eb2e2e"}
Area2 Global/EU-Demo Area2-BLD1 180 West Tasman Drive, San Jose 95134
{"type": "building", "site": {"area": {"name": "Area2", "parentName": "Global/EU-Demo"}, "building": {"name": "Area2-BLD1", "address": "180 West Tasman Drive, San Jose 95134"}}}
{"result": {"result": {"startTime": 1582780990575, "endTime": 1582780990626, "progress": "Site Creation completed successfully"}}, "status": "True", "siteId": "2eac5fc9-204b-4a77-8b25-e9a29aef0026"}
Area3 Global/EU-Demo Area3-BLD1 190 West Tasman Drive, San Jose 95134
{"type": "building", "site": {"area": {"name": "Area3", "parentName": "Global/EU-Demo"}, "building": {"name": "Area3-BLD1", "address": "190 West Tasman Drive, San Jose 95134"}}}
{"result": {"result": {"startTime": 1582780992101, "endTime": 1582780992144, "progress": "Site Creation completed successfully"}}, "status": "True", "siteId": "d3f2ddca-de99-47c7-b202-39a256c8b7d2"}
Area3 Global/EU-Demo Area3-BLD2 191 West Tasman Drive, San Jose 95134
{"type": "building", "site": {"area": {"name": "Area3", "parentName": "Global/EU-Demo"}, "building": {"name": "Area3-BLD2", "address": "191 West Tasman Drive, San Jose 95134"}}}
{"result": {"result": {"startTime": 1582780993502, "endTime": 1582780993543, "progress": "Site Creation completed successfully"}}, "status": "True", "siteId": "9456baba-4fa1-4a6e-be50-b6a5f0b90a4d"}

-- Building Creation complete 

-- Site Creation complete

**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
