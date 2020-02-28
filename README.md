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
{
    "type" : "area" , 
    "site" : {
        "area" : {
            "name" : "EU-Demo" , 
            "parentName" : "Global"
        }
    }
}
{
    "result" : {
        "result" : {
            "startTime" : 1582849978994 , 
            "endTime" : 1582849979019 , 
            "progress" : "Site Creation completed successfully"
        }
    } , 
    "status" : "True" , 
    "siteId" : "390ec961-7ce4-4d56-bb8b-ac0d8e93f2e8"
}
Area1 Global/EU-Demo
{
    "type" : "area" , 
    "site" : {
        "area" : {
            "name" : "Area1" , 
            "parentName" : "Global/EU-Demo"
        }
    }
}
{
    "result" : {
        "result" : {
            "startTime" : 1582849979794 , 
            "endTime" : 1582849979908 , 
            "progress" : "Site Creation completed successfully"
        }
    } , 
    "status" : "True" , 
    "siteId" : "1be68b5e-cc6a-4396-902a-f66346a83b69"
}
Area2 Global/EU-Demo
{
    "type" : "area" , 
    "site" : {
        "area" : {
            "name" : "Area2" , 
            "parentName" : "Global/EU-Demo"
        }
    }
}
{
    "result" : {
        "result" : {
            "startTime" : 1582849980797 , 
            "endTime" : 1582849980823 , 
            "progress" : "Site Creation completed successfully"
        }
    } , 
    "status" : "True" , 
    "siteId" : "8c73b511-86be-49ef-aee0-0eb49c07ee2a"
}
Area3 Global/EU-Demo
{
    "type" : "area" , 
    "site" : {
        "area" : {
            "name" : "Area3" , 
            "parentName" : "Global/EU-Demo"
        }
    }
}
{
    "result" : {
        "result" : {
            "startTime" : 1582849981598 , 
            "endTime" : 1582849981627 , 
            "progress" : "Site Creation completed successfully"
        }
    } , 
    "status" : "True" , 
    "siteId" : "f4fdafbc-9ea6-4728-82bb-c456f0e78304"
}

-- Area Creation complete

Area1 Global/EU-Demo Area1-BLD1 170 West Tasman Drive, San Jose 95134
{
    "type" : "building" , 
    "site" : {
        "area" : {
            "name" : "Area1" , 
            "parentName" : "Global/EU-Demo"
        } , 
        "building" : {
            "name" : "Area1-BLD1" , 
            "address" : "170 West Tasman Drive, San Jose 95134"
        }
    }
}
{
    "result" : {
        "result" : {
            "startTime" : 1582849982782 , 
            "endTime" : 1582849982818 , 
            "progress" : "Site Creation completed successfully"
        }
    } , 
    "status" : "True" , 
    "siteId" : "98791422-c35c-4335-9406-56b6e6fc2674"
}
Area1 Global/EU-Demo Area1-BLD2 171 West Tasman Drive, San Jose 95134
{
    "type" : "building" , 
    "site" : {
        "area" : {
            "name" : "Area1" , 
            "parentName" : "Global/EU-Demo"
        } , 
        "building" : {
            "name" : "Area1-BLD2" , 
            "address" : "171 West Tasman Drive, San Jose 95134"
        }
    }
}
{
    "result" : {
        "result" : {
            "startTime" : 1582849983665 , 
            "endTime" : 1582849983715 , 
            "progress" : "Site Creation completed successfully"
        }
    } , 
    "status" : "True" , 
    "siteId" : "8bdcf297-5991-4ecd-9e33-389995e51c09"
}
Area2 Global/EU-Demo Area2-BLD1 180 West Tasman Drive, San Jose 95134
{
    "type" : "building" , 
    "site" : {
        "area" : {
            "name" : "Area2" , 
            "parentName" : "Global/EU-Demo"
        } , 
        "building" : {
            "name" : "Area2-BLD1" , 
            "address" : "180 West Tasman Drive, San Jose 95134"
        }
    }
}
{
    "result" : {
        "result" : {
            "startTime" : 1582849984578 , 
            "endTime" : 1582849984719 , 
            "progress" : "Site Creation completed successfully"
        }
    } , 
    "status" : "True" , 
    "siteId" : "af375831-f269-45b0-8876-fb82367a6750"
}
Area3 Global/EU-Demo Area3-BLD1 190 West Tasman Drive, San Jose 95134
{
    "type" : "building" , 
    "site" : {
        "area" : {
            "name" : "Area3" , 
            "parentName" : "Global/EU-Demo"
        } , 
        "building" : {
            "name" : "Area3-BLD1" , 
            "address" : "190 West Tasman Drive, San Jose 95134"
        }
    }
}
{
    "result" : {
        "result" : {
            "startTime" : 1582849985680 , 
            "endTime" : 1582849985716 , 
            "progress" : "Site Creation completed successfully"
        }
    } , 
    "status" : "True" , 
    "siteId" : "54efbce8-5252-46a2-a146-930d607cbcfe"
}
Area3 Global/EU-Demo Area3-BLD2 191 West Tasman Drive, San Jose 95134
{
    "type" : "building" , 
    "site" : {
        "area" : {
            "name" : "Area3" , 
            "parentName" : "Global/EU-Demo"
        } , 
        "building" : {
            "name" : "Area3-BLD2" , 
            "address" : "191 West Tasman Drive, San Jose 95134"
        }
    }
}
{
    "result" : {
        "result" : {
            "startTime" : 1582849986493 , 
            "endTime" : 1582849986520 , 
            "progress" : "Site Creation completed successfully"
        }
    } , 
    "status" : "True" , 
    "siteId" : "bebcbf96-78cb-4c1c-864e-a75d6c9838ce"
}

-- Building Creation complete 

-- Site Creation complete

**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).
