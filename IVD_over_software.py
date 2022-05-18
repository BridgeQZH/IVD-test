def IVD_software(DID):
    class Software:
        def __init__(self, DID):
            self.DID = DID
            self.DID1_status = DID[0]
            self.DID1_content = DID[1]
            self.DID2_status = DID[2]
            self.DID2_content = DID[3]
            self.DID3_status = DID[4]
            self.DID3_content = DID[5]
            self.DID4_status = DID[6]
            self.DID4_content = DID[7]     
            self.DID5_status = DID[8]
            self.DID5_content = DID[9]

        def __hash__(self):
            # print('The hash for this software setting is:')
            # print(hash(self.DID1_status or self.DID1_content))
            return hash("abc")


    settings2 = Software(DID)
    return(settings2.__hash__())

