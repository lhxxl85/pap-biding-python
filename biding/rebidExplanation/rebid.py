from biding.utils.validate import Validate

class RebidExplanation:
  def __init__(self, reason = '', 
  eventTime = None, awareTime = None, 
  decisionTime = None, category = None):
    self.reason = reason
    self.eventTime = eventTime
    self.awareTime = awareTime
    self.decisionTime = decisionTime
    self.category = category
  
  def ValidRebitExplanation(self):
    return Validate(self)
  
  def reprJSON(self):
    jsondict = dict(reason = self.reason, eventTime = self.eventTime, 
    awareTime = self.awareTime, decisionTime = self.decisionTime,
    category = self.category)
    jsonkeys = jsondict.keys()
    for i in list(jsonkeys):
      if jsondict[i] == None or jsondict[i] == '' or (isinstance(jsondict[i], list) and len(jsondict[i])==0):
        del jsondict[i]
    return jsondict
