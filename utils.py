import configparser
from sumolib import checkBinary
import os
import sys


def import_test_configuration(config_file):
    """
    Read the config file regarding the testing and import its content
    """
    content = configparser.ConfigParser()
    content.read(config_file)
    config = {}
    config['DID1'] = content['parameters'].getboolean('DID1')
    config['DID1_content'] = content['parameters'].getint('DID1_content')
    config['DID2'] = content['parameters'].getboolean('DID2')
    config['DID2_content'] = content['parameters'].get('DID2_content')
    config['DID3'] = content['parameters'].getboolean('DID3')
    config['DID3_content'] = content['parameters'].getint('DID3_content')
    config['DID4'] = content['parameters'].getboolean('DID4')
    config['DID4_content'] = content['parameters'].get('DID4_content')
    config['DID5'] = content['parameters'].getboolean('DID5')
    config['DID5_content'] = content['parameters'].get('DID5_content')
    config['name_software'] = content['software'].get('name_software')
    config['version_number'] = content['software'].getfloat('version_number')
    return config