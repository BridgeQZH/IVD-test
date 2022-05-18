def IVD_software(flash):
    class Software:
        def __init__(self, flash):
            self.company = flash[0]
            self.version_number = flash[1]
            

        def __hash__(self):
            # print('The hash for this software setting is:')
            # print(hash(self.DID1_status or self.DID1_content))
            return hash((self.company, self.version_number))


    settings2 = Software(flash)
    return(settings2.__hash__())

