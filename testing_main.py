from IVD_over_parameters import IVD_parameters
from IVD_over_software import IVD_software
from IVD_whole import IVD
from utils import import_test_configuration

if __name__ == "__main__":
    config = import_test_configuration(config_file='testing_settings.ini')
    DID = [config['DID1'], config['DID1_content'],\
           config['DID2'], config['DID2_content'],\
           config['DID3'], config['DID3_content'],\
           config['DID4'], config['DID4_content'],\
           config['DID5'], config['DID5_content']]
    flash = [config['name_software'], config['version_number']]

    a = IVD_parameters(DID)
    print('The hash for this parameter setting is:')
    print(a)

    b = IVD_software(flash)
    print('The hash for this software setting is:')
    print(b)

    final_IVD_value = IVD(a, b)
    print('The hash for whole settings is:')
    print(final_IVD_value)

    ## Publish this IVD to CAN or UDS ##
