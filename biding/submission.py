from biding.utils.validate import Validate

class Submission:
  def __init__(self):
    self.submissionTimeStamp = ""
    self.referenceId = None
    self.comment = ""
    self.authorisedBy = ""
    self.energyBids = []
    self.fcasBids = []
    self.mnspBids = []

  def ValidateSubmission(self):
    return Validate(self)

  def reprJSON(self):
    jsondict = dict(submissionTimeStamp = self.submissionTimeStamp,
    referenceId = self.referenceId, comment = self.comment,
    authorisedBy = self.authorisedBy, energyBids = self.energyBids,
    fcasBids = self.fcasBids, mnspBids = self.mnspBids)
    jsonkeys = jsondict.keys()
    for i in list(jsonkeys):
      if jsondict[i] == None or jsondict[i] == '' or (isinstance(jsondict[i], list) and len(jsondict[i])==0):
        del jsondict[i]
    return jsondict