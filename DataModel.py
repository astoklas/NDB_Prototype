__author__ = 'astoklas'

import json

ns0_deviceConfig = {
    'creatorRole': '',
    'name': '',
    'creatorUser': '',
    'nodeConnector': '',
    'icon': ''
}

deviceConfig_creatorRole_Admin = "Network-Admin"
deviceConfig_creatorRole_User = "Network-User"
deviceConfig_icon1 = "monitor1"
deviceConfig_icon2 = "monitor2"
deviceConfig_icon3 = "monitor3"
deviceConfig_icon4 = "monitor4"
deviceConfig_icon5 = "monitor5"

ns0_portConfig = {
    'nodeConnector': '',
    'timeStampTagging': '',
    'truncate': '',
    'monitorPortType': '',
    'vlanTag': '',
    'description': '',
    'spanDestination': ''
}

ns0_matchConfig = {
    'vlanPriority': '',
    'tcpOptionLength': '',
    'vlanId': '',
    'name': '',
    'tosBits': '',
    'networkDst': '',
    'transportPortDst': '',
    'datalayerSrc': '',
    'datalayerDst': '',
    'httpMethodId': '',
    'transportPortSrc': '',
    'networkSrc': '',
    'etherType': '',
    'bidirectional': '',
    'protocol': ''
}

ns0_redirectionsConfig = {
    'autoPriority': '',                 # (string, optional),
    'productionEgress': '',             # (string, optional),
    'name': '',                         # (string, optional),
    'backupBypass': '',                 # (string, optional),
    'installInHw': '',                  # (string, optional),
    'serviceNode': '',                  # (List[string], optional),
    'priority': '',                     # (string, optional),
    'filter': '',                       # (string, optional),
    'description': '',                  # (string, optional),
    'productionIngress': '',            # (List[string], optional),
    'allowFilter': '',                  # (List[string], optional),
    'device': ''                        # (List[string], optional)
}

ns0_serviceNodeConfig = {
    'name': '',                         # (string, optional),
    'serviceNodeIngressConnector': '',  # (string, optional),
    'creatorRole': '',                  # (string, optional),
    'serviceNodeEgressConnector': '',   # (string, optional),
    'creatorUser': '',                  # (string, optional),
    'icon': ''                          # (string, optional)
}

ns0_roleConfig = {
    'role': '',                         # (string, optional),
    'level': '',                        # (string, optional)
}

etherType_IP = '0x0800'
protocol_tcp = '6'
protocol_udp = '17'

deviceConfig = ns0_deviceConfig.copy()
deviceConfig['creatorRole'] = "Test2"

print deviceConfig
print json.dumps(deviceConfig)

