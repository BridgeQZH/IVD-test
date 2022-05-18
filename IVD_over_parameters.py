class Parameters:
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
        print('The hash for this setting is:')
        return hash(tuple(self.DID))

DID1 = True
DID1_content = 123
DID2 = False
DID2_content = "4db5"
DID3 = False
DID3_content = 456
DID4 = False
DID4_content = (3,3)
DID5 = True
DID5_content = "abc"
DID = [DID1, DID1_content, DID2, DID2_content, DID3, DID3_content, DID4, DID4_content, DID5, DID5_content]

settings1 = Parameters(DID)
print(settings1.__hash__())

