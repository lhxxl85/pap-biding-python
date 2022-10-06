from biding.energyBid.energyBid import EnergyBid, FastStartProfile, EnergyPeriod
from biding.fcasBid.fcasBid import FcasBid, FcasPeriod
from biding.mnspBid.mnspBid import MnspBid, MnspBidLink, MnspPeriod
from biding.rebidExplanation.rebid import RebidExplanation
import json
from biding.utils.jsonParser import ComplexEncoder
from biding.submission import Submission
import datetime
import random

def main():
  fastStartProfile = FastStartProfile()
  fastStartProfile.minimumLoad = random.randint(0, 99)
  fastStartProfile.t1 = random.randint(0, 30)
  fastStartProfile.t2 = random.randint(0, 30)
  fastStartProfile.t3 = random.randint(0, 59)
  fastStartProfile.t4 = random.randint(0, 59)
  datenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  bid = EnergyBid(datenow, 'ABCDEIGHIJ')
  fcasbid = FcasBid(datenow, 'ABCDEIGHIJ')
  mnspbid = MnspBid(datenow, 'ABCDEIGHIJ')
  mnspbidlink = MnspBidLink('FFFFFFFFFF')
  rebid = RebidExplanation('For Test')
  for i in range(10):
    bid.AppendPrice(round(random.uniform(1, 99), 2))
    fcasbid.AppendPrice(round(random.uniform(1, 99), 2))
    mnspbidlink.AppendPrice(round(random.uniform(1, 99), 2))
  bid.AttachFastStartProfile(fastStartProfile)
  for i in range(288):
    period = MnspPeriod()
    period.periodId = i+1
    band = []
    for j in range(10):
      band.append(random.randint(1, 10))
    period.bandAvail = band
    period.maxAvail = random.randint(0, 99)
    period.passAvail = random.randint(0, 99)
    period.rampUpRate = random.randint(0, 99)
    period.mrCapacity = random.randint(0, 99)
    period.fixedLoad = random.randint(1, 99)
    mnspbidlink.AppendPeriod(period)
  mnspbid.mnspBidExport = mnspbidlink
  mnspbid.mnspBidImport = mnspbidlink
  bid.energyPeriods = None
  for i in range(288):
    period = EnergyPeriod()
    period.periodId = i+1
    band = []
    for j in range(10):
      band.append(random.randint(1, 10))
    period.bandAvail = band
    period.maxAvail = random.randint(0, 99)
    period.passAvail = random.randint(0, 99)
    period.rampUpRate = random.randint(0, 99)
    period.rampDownRate = random.randint(0, 99)
    period.mrCapacity = random.randint(0, 99)
    period.fixedLoad = random.randint(1, 99)
    bid.AppendPeriod(period)
  for i in range(288):
    period = FcasPeriod()
    period.periodId = i+1
    band = []
    for j in range(10):
      band.append(random.randint(1, 10))
    period.bandAvail = band
    period.maxAvail = random.randint(0, 99)
    period.enablementMin = random.randint(0, 99)
    period.enablementMax = random.randint(0, 99)
    period.lowBreakPoint = random.randint(0, 99)
    period.highBreakPoint = random.randint(0, 99)
    fcasbid.AppendPeriod(period)
  fcasbid.service = 'RAISE6SEC'
  submit = Submission()
  bid.rebidExplanation = rebid
  submit.energyBids.append(bid)
  submit.fcasBids.append(fcasbid)
  submit.mnspBids.append(mnspbid)
  submit.referenceId = '000000000'
  if submit.ValidateSubmission():
    submitstr = json.dumps(submit.reprJSON(), cls=ComplexEncoder)
    with open('api.json', 'w') as f:
      f.write(submitstr)

if __name__ == '__main__':
  main()