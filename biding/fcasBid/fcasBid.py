from biding.utils.validate import Validate

class FcasBid:
  def __init__(self, tradingDate = '', duid = '', prices = None, fcasPeriods = [],
  rebidExplanation = '', service = ''):
    self.tradingDate = tradingDate
    self.duid = duid
    self.prices = prices
    self.service = service
    self.fcasPeriods = fcasPeriods
    self.rebidExplanation = rebidExplanation
  
  def AppendPeriod(self, period):
    if self.fcasPeriods == None:
      self.fcasPeriods = []
    if isinstance(period, FcasPeriod):
      self.fcasPeriods.append(period)

  def AttachPricesList(self, prices):
    if isinstance(prices, list):
        self.prices = prices

  def AttachFcasPeriods(self, periods):
    self.fcasPeriods = []
    if isinstance(periods, list):
      for item in periods:
        if isinstance(item, FcasPeriod):
          self.fcasPeriods.append(item)

  def AppendPrice(self,price):
    if self.prices == None:
      self.prices = []
    if isinstance(price, int):
      price = round(float(price),2)
      self.prices.append(price)
      return
    if isinstance(price, float):
      price = round(price, 2)
      self.prices.append(price)
      return
    if isinstance(price,str):
      price = round(float(price),2)
      self.prices.append(price)
      return

  def reprJSON(self):
    jsondict = dict(tradingDate = self.tradingDate, duid = self.duid, prices = self.prices,
    service = self.service, fcasPeriods = self.fcasPeriods, rebidExplanation = self.rebidExplanation)
    jsonkeys = jsondict.keys()
    for i in list(jsonkeys):
      if jsondict[i] == None or jsondict[i] == '' or (isinstance(jsondict[i], list) and len(jsondict[i])==0):
        del jsondict[i]
    return jsondict
  
  def ValidFcasBid(self):
    return Validate(self)


class FcasPeriod:
  def __init__(self, periodId = 0, bandAvail = None, maxAvail = '', enablementMin = '', enablementMax = '', lowBreakPoint = '',
  highBreakPoint = ''):
    self.periodId = periodId
    self.bandAvail = bandAvail
    self.maxAvail = maxAvail
    self.enablementMin = enablementMin
    self.enablementMax = enablementMax
    self.lowBreakPoint = lowBreakPoint
    self.highBreakPoint = highBreakPoint
  
  def ValidFcasPeriod(self):
    return Validate(self)
  
  def reprJSON(self):
    jsondict = dict(periodId = self.periodId, bandAvail = self.bandAvail, 
    maxAvail = self.maxAvail, enablementMin = self.enablementMin, enablementMax = self.enablementMax,
    lowBreakPoint = self.lowBreakPoint, highBreakPoint = self.highBreakPoint)
    jsonkeys = jsondict.keys()
    for i in list(jsonkeys):
      if jsondict[i] == None or jsondict[i] == '' or (isinstance(jsondict[i], list) and len(jsondict[i])==0):
        del jsondict[i]
    return jsondict