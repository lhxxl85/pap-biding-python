SubmissionRule = [
  {
    'name': 'submissionTimeStamp',
    'required': False,
    'validator': {
      'type': 'datetime',
      'format': '%Y-%m-%dT%H:%M:%S+%H:%M'
    }
  },
  {
    'name': 'referenceId',
    'required': True,
    'validator': {
      'type': 'string',
      'maxLength': 100,
    }
  },
  {
    'name': 'comment',
    'required': False,
    'validator': {
      'type': 'string',
      'maxLength': 100
    }
  },
  {
    'name': 'authorisedBy',
    'required': False,
    'validator': {
      'type': 'string',
      'maxLength': 20
    }
  },
  {
    'name': 'energyBids',
    'required': False,
    'validator': {
      'type': 'array',
      'itemValidator': {
        'type': 'object',
        'objectReference': 'EnergyBid'
      }
    }
  },
  {
    'name': 'fcasBids',
    'required': False,
    'validator': {
      'type': 'array',
      'itemValidator': {
        'type': 'object',
        'objectReference': 'FcasBid'
      }
    }
  },
    {
    'name': 'mnspBids',
    'required': False,
    'validator': {
      'type': 'array',
      'itemValidator': {
        'type': 'object',
        'objectReference': 'MnspBid'
      }
    }
  }
]

EnergyBidRule = [
  {
    'name': 'tradingDate',
    'validator': {
      'type': 'datetime',
      'format': '%Y-%m-%d %H:%M:%S'
    },
    'required': True
  }, 
  {
    'name': 'duid',
    'validator': {
      'type': 'string',
      'maxLength': 10,
      'strtype': 'uppercase'
    },
    'required': True
  },
  {
    'name': 'fastStartProfile',
    'required': False,
    'validator': {
      'type': 'object',
      'objectReference': 'FastStartProfile'
    }
  }, 
  {
    'name': 'prices',
    'required': True,
    'validator': {
      'type': 'array',
      'minLength': 10,
      'maxLength': 10,
      'itemValidator': {
        'type': 'number'
      }
    }
  }, 
  {
    'name': 'mrPriceScalingFactor',
    'required': False,
    'validator' : {
      'type': 'number',
      'minimum': 0
    }
  },
  {
    'name': 'dailyEnergyConstraint',
    'required': False,
    'validator' : {
      'type': 'integer',
      'minimum': 0,
      'maximum': 999999
    }
  },
  {
    'name':'energyPeriods',
    'required': True,
    'validator': {
      'type': 'array',
      'minLength': 288,
      'maxLength': 288,
      'itemValidator': {
        'type': 'object',
        'objectReference': 'EnergyPeriod'
      }
    }
  },
  {
    'name': 'rebidExplanation',
    'required': False,
    'validator': {
      'type': 'object',
      'objectReference': 'RebidExplanation' 
    }
  }
]

FastStartProfileRule = [
  {
    'name': 'minimumLoad',
    'required': True,
    'validator': {
      'type': 'number',
      'minimum': 0
    }
  },
  {
    'name': 't1',
    'required': True,
    'validator': {
      'type': 'number',
      'minimum': 0,
      'maximum': 30
    }
  },
  {
    'name': 't2',
    'required': True,
    'validator': {
      'type': 'number',
      'minimum': 0,
      'maximum': 30
    }
  },
  {
    'name': 't3',
    'required': True,
    'validator': {
      'type': 'number',
      'minimum': 0,
      'maximum': 59
    }
  },
  {
    'name': 't4',
    'required': True,
    'validator': {
      'type': 'number',
      'minimum': 0,
      'maximum': 59
    }
  },
]

EnergyPeriodRule = [
  {
    'name': 'periodId',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 1,
      'maximum': 288
    }
  },
  {
    'name': 'bandAvail',
    'required': True,
    'validator': {
      'type': 'array',
      'maxLength': 10,
      'minLength': 10,
      'itemValidator': {
        'type': 'integer',
        'minimum': 0
      }
    }
  },
  {
    'name': 'maxAvail',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'passAvail',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'rampUpRate',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'rampDownRate',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'mrCapacity',
    'required': False,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'fixedLoad',
    'required': False,
    'validator': {
      'type': 'integer',
      'minimum': 1
    }
  }
]

RebidExplanationRule = [
  {
    'name': 'reason',
    'required': True,
    'validator': {
      'type': 'string',
      'maxLength': 500
    }
  },
  {
    'name': 'eventTime',
    'required': False,
    'validator': {
      'type': 'datetime',
      'format': '%H:%M:%S'
    }
  },
  {
    'name': 'awareTime',
    'required': False,
    'validator': {
      'type': 'datetime',
      'format': '%H:%M:%S'
    }
  },
  {
    'name': 'decisionTime',
    'required': False,
    'validator': {
      'type': 'datetime',
      'format': '%H:%M:%S'
    }
  },
  {
    'name': 'category',
    'required': False,
    'validator': {
      'type': 'string',
      'maxLength': 1
    }
  }
]

FcasBidRule = [
  {
    'name': 'tradingDate',
    'validator': {
      'type': 'datetime',
      'format': '%Y-%m-%d %H:%M:%S'
    },
    'required': True
  }, 
  {
    'name': 'duid',
    'validator': {
      'type': 'string',
      'maxLength': 10,
      'strtype': 'uppercase',
      
    },
    'required': True
  },
  {
    'name': 'service',
    'required': True,
    'validator': {
      'type': 'enum',
      'enum': [
        'RAISE6SEC',
        'RAISE60SEC',
        'RAISE5MIN',
        'RAISEREG',
        'LOWER6SEC',
        'LOWER60SEC',
        'LOWER5MIN',
        'LOWERREG'
      ]
    }
  }, 
  {
    'name': 'prices',
    'required': True,
    'validator': {
      'type': 'array',
      'minLength': 10,
      'maxLength': 10,
      'itemValidator': {
        'type': 'number'
      }
    }
  }, 
  {
    'name':'fcasPeriods',
    'required': True,
    'validator': {
      'type': 'array',
      'minLength': 288,
      'maxLength': 288,
      'itemValidator': {
        'type': 'object',
        'objectReference': 'FcasPeriod'
      }
    }
  },
  {
    'name': 'rebidExplanation',
    'required': False,
    'validator': {
      'type': 'object',
      'objectReference': 'RebidExplanation' 
    }
  }  
]

FcasPeriodRule = [
  {
    'name': 'periodId',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 1,
      'maximum': 288
    }
  },
  {
    'name': 'bandAvail',
    'required': True,
    'validator': {
      'type': 'array',
      'maxLength': 10,
      'minLength': 10,
      'itemValidator': {
        'type': 'integer',
        'minimum': 0
      }
    }
  },
  {
    'name': 'maxAvail',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'enablementMin',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'enablementMax',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'lowBreakPoint',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'highBreakPoint',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  }
]

MnspPeriodRule = [
  {
    'name': 'periodId',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 1,
      'maximum': 288
    }
  },
  {
    'name': 'bandAvail',
    'required': True,
    'validator': {
      'type': 'array',
      'maxLength': 10,
      'minLength': 10,
      'itemValidator': {
        'type': 'integer',
        'minimum': 0
      }
    }
  },
  {
    'name': 'maxAvail',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'passAvail',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'rampUpRate',
    'required': True,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'mrCapacity',
    'required': False,
    'validator': {
      'type': 'integer',
      'minimum': 0
    }
  },
  {
    'name': 'fixedLoad',
    'required': False,
    'validator': {
      'type': 'integer',
      'minimum': 1
    }
  }
]

MnspBidRule = [
  {
    'name': 'interconnectorId',
    'validator': {
      'type': 'string',
      'maxLength': 10,
    },
    'required': True
  },
  {
    'name': 'tradingDate',
    'validator': {
      'type': 'datetime',
      'format': '%Y-%m-%d %H:%M:%S'
    },
    'required': True
  },
  {
    'name': 'mnspBidImport',
    'required': True,
    'validator': {
      'type': 'object',
      'objectReference': 'MnspBidLink'
    }
  },
  {
    'name': 'mnspBidExport',
    'required': True,
    'validator': {
      'type': 'object',
      'objectReference': 'MnspBidLink'
    }
  },
  {
    'name': 'rebidExplanation',
    'required': False,
    'validator': {
      'type': 'object',
      'objectReference': 'RebidExplanation' 
    }
  }
]

MnspBidLinkRule = [
  {
    'name': 'linkId',
    'validator': {
      'type': 'string',
      'maxLength': 10,
    },
    'required': True
  },
  {
    'name': 'prices',
    'required': True,
    'validator': {
      'type': 'array',
      'minLength': 10,
      'maxLength': 10,
      'itemValidator': {
        'type': 'number'
      }
    }
  }, 
  {
    'name':'mnspPeriods',
    'required': True,
    'validator': {
      'type': 'array',
      'minLength': 288,
      'maxLength': 288,
      'itemValidator': {
        'type': 'object',
        'objectReference': 'MnspPeriod'
      }
    }
  },
  {
    'name': 'mrPriceScalingFactor',
    'required': False,
    'validator' : {
      'type': 'number',
      'minimum': 0
    }
  }
]

