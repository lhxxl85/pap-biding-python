from ..utils.validate import Validate

class EnergyPeriod:
  def __init__(self, periodId = 0, bandAvail = None, maxAvail = '', passAvail = '', rampUpRate = '', rampDownRate = '',
  fixedLoad = '', mrCapacity = None):
    self.periodId = periodId
    self.bandAvail = bandAvail
    self.maxAvail = maxAvail
    self.passAvail = passAvail
    self.rampUpRate = rampUpRate
    self.rampDownRate = rampDownRate
    self.fixedLoad = fixedLoad
    self.mrCapacity = mrCapacity

  def ValidPeriod(self):
    return Validate(self)
  
  def reprJSON(self):
    jsondict = dict(periodId = self.periodId, bandAvail = self.bandAvail, 
    maxAvail = self.maxAvail, passAvail = self.passAvail, rampUpRate = self.rampUpRate,
    rampDownRate = self.rampDownRate, fixedLoad = self.fixedLoad, mrCapacity = self.mrCapacity)
    jsonkeys = jsondict.keys()
    for i in list(jsonkeys):
      if jsondict[i] == None or jsondict[i] == '' or (isinstance(jsondict[i], list) and len(jsondict[i])==0):
        del jsondict[i]
    return jsondict

class FastStartProfile:
  def __init__(self,minimumLoad = None, t1 = None, t2 = None, t3 = None, t4 = None):
    self.minimumLoad = minimumLoad
    self.t1 = t1
    self.t2 = t2
    self.t3 = t3
    self.t4 = t4
  
  def ValidFastStartProfile(self):
    return Validate(self)

  def reprJSON(self):
    return dict(miniLoad = self.minimumLoad, t1 = self.t1, t2 = self.t2, t3 = self.t3, t4 = self.t4)
  

class EnergyBid:
  def __init__(self, tradingDate = '', duid = '', prices = None, energyPeriods = [], fastStartProfile= None, dailyEnergyConstraint = '',
  rebidExplanation = '', mrPriceScalingFactor = ''):
    self.tradingDate = tradingDate
    self.duid = duid
    self.prices = prices
    self.fastStartProfile = fastStartProfile
    self.dailyEnergyConstraint = dailyEnergyConstraint
    self.rebidExplanation = rebidExplanation
    self.mrPriceScalingFactor = mrPriceScalingFactor
    self.energyPeriods = energyPeriods

  def reprJSON(self):
    jsondict = dict(tradingDate = self.tradingDate, duid = self.duid, prices = self.prices,
    fastStartProfile = self.fastStartProfile, dailyEnergyConstraint = self.dailyEnergyConstraint, rebidExplanation = self.rebidExplanation,
    mrPriceScalingFactor = self.mrPriceScalingFactor, energyPeriods = self.energyPeriods)
    jsonkeys = jsondict.keys()
    for i in list(jsonkeys):
      if jsondict[i] == None or jsondict[i] == '' or (isinstance(jsondict[i], list) and len(jsondict[i])==0):
        del jsondict[i]
    return jsondict

  def AttachFastStartProfile(self,fastStartProfile):
    if isinstance(fastStartProfile, FastStartProfile):
      self.fastStartProfile = fastStartProfile
  
  def AppendPeriod(self, period):
    if self.energyPeriods == None:
      self.energyPeriods = []
    if isinstance(period, EnergyPeriod):
      self.energyPeriods.append(period)

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

  def AttachEnergyPeriods(self, periods):
    self.energyPeriods = []
    if isinstance(periods, list):
      for item in periods:
        if isinstance(item, EnergyPeriod):
          self.energyPeriods.append(item)
  
  def ValidEnergyBid(self):
    return Validate(self)

