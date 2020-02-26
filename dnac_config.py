"""

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Saurav Prasad TME, IBNG"
__email__ = "saurav@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


# This file contains the:
# Cisco DNA Center username and password, server info

# Update this section with the Cisco DNA Center server info and user information

import os

DNAC=os.environ.get('DNAC','DNAC_URL')
DNAC_PORT=os.environ.get('DNAC_PORT',443)
DNAC_USER=os.environ.get('DNAC_USER','username')
DNAC_PASSWORD=os.environ.get('DNAC_PASSWORD','password')
