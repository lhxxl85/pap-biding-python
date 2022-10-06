from biding.utils.validate import Validate

class MnspBid:
  def __init__(self, tradingDate = '', interconnectorId = '', mnspBidImport = None,
  mnspBidExport = None, rebidExplanation = None ):
    self.interconnectorId = interconnectorId
    self.tradingDate = tradingDate
    self.mnspBidImport = mnspBidImport
    self.mnspBidExport = mnspBidExport
    self.rebidExplanation = rebidExplanation
  
  def ValidMnspBid(self):
    return Validate(self)
  
  def reprJSON(self):
    jsondict = dict(interconnectorId = self.interconnectorId, tradingDate = self.tradingDate, 
    mnspBidImport = self.mnspBidImport, mnspBidExport = self.mnspBidExport, rebidExplanation = self.rebidExplanation)
    jsonkeys = jsondict.keys()
    for i in list(jsonkeys):
      if jsondict[i] == None or jsondict[i] == '' or (isinstance(jsondict[i], list) and len(jsondict[i])==0):
        del jsondict[i]
    return jsondict

class MnspBidLink:
  def __init__(self, linkId = '', prices = [], mnspPeriods = None, mrPriceScalingFactor = None):
    self.linkId = linkId
    self.prices = prices
    self.mnspPeriods = mnspPeriods
    self.mrPriceScalingFactor = mrPriceScalingFactor

  def reprJSON(self):
    jsondict = dict(linkId = self.linkId, prices = self.prices, 
    mnspPeriods = self.mnspPeriods, mrPriceScalingFactor = self.mrPriceScalingFactor)
    jsonkeys = jsondict.keys()
    for i in list(jsonkeys):
      if jsondict[i] == None or jsondict[i] == '' or (isinstance(jsondict[i], list) and len(jsondict[i])==0):
        del jsondict[i]
    return jsondict

  def AppendPeriod(self, period):
    if self.mnspPeriods == None:
      self.mnspPeriods = []
    if isinstance(period, MnspPeriod):
      self.mnspPeriods.append(period)
  
  def AttachMnspPeriods(self, periods):
    self.mnspPeriods = []
    if isinstance(periods, list):
      for item in periods:
        if isinstance(item, MnspPeriod):
          self.mnspPeriods.append(item)
  
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

  def AttachPricesList(self, prices):
    if isinstance(prices, list):
        self.prices = prices

  def ValidMnspBid(self):
    return Validate(self)

class MnspPeriod:
  def __init__(self, periodId = 0, bandAvail = None, maxAvail = '', passAvail = '', rampUpRate = '', rampDownRate = '',
  fixedLoad = '', mrCapacity = None):
    self.periodId = periodId
    self.bandAvail = bandAvail
    self.maxAvail = maxAvail
    self.passAvail = passAvail
    self.rampUpRate = rampUpRate
    self.fixedLoad = fixedLoad
    self.mrCapacity = mrCapacity
  
  def ValidPeriod(self):
    return Validate(self)
  
  def reprJSON(self):
    jsondict = dict(periodId = self.periodId, bandAvail = self.bandAvail, 
    maxAvail = self.maxAvail, passAvail = self.passAvail, rampUpRate = self.rampUpRate,
    fixedLoad = self.fixedLoad, mrCapacity = self.mrCapacity)
    jsonkeys = jsondict.keys()
    for i in list(jsonkeys):
      if jsondict[i] == None or jsondict[i] == '' or (isinstance(jsondict[i], list) and len(jsondict[i])==0):
        del jsondict[i]
    return jsondict  