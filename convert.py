from lxml import etree

parser = etree.XMLParser(ns_clean=False)

tree = etree.parse('/Users/gary/Downloads/CIS_Red_Hat_EL7_Server_L1_v2.2.0.audit', parser)

etree.tostring(tree)
