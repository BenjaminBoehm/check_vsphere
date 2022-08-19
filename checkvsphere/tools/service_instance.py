"""
This module implements simple helper functions for managing service instance objects

"""
# VMware vSphere Python SDK Community Samples Addons
# Copyright (c) 2014-2021 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# See LICENSE-VMWARE

__author__ = "VMware, Inc."

import atexit
from pyVim.connect import SmartConnect, Disconnect


def connect(args):
    """
    Determine the most preferred API version supported by the specified server,
    then connect to the specified server using that API version, login and return
    the service instance object.
    """

    service_instance = None

    # form a connection...
    if args.disable_ssl_verification:
        service_instance = SmartConnect(host=args.host,
                                        user=args.user,
                                        pwd=args.password,
                                        port=args.port,
                                        disableSslCertValidation=True)
    else:
        service_instance = SmartConnect(host=args.host,
                                        user=args.user,
                                        pwd=args.password,
                                        port=args.port)

    # doing this means you don't need to remember to disconnect your script/objects
    atexit.register(Disconnect, service_instance)

    return service_instance
