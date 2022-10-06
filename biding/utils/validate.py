import time
from ..error.bidingError import *
import biding.utils.validateRule as validateRule
from termcolor import colored

def isDatetime(datestr, format):
  if len(datestr) == 25:
    datetime = datestr[:19]
    datetimezone = datestr[19:]
    try:
      time.strptime(datetime, format[:19])
    except:
      print('Time stamp is not valid format.')
      return -1
    try:
      time.strptime(datetimezone, format[19:])
    except:
      print('Time stamp time zone is not valid.')
      return -1
    return 0
  if len(datestr) == 19:
    datetime = datestr[:19]
    try:
      time.strptime(datetime, format)
    except:
      print('Time stamp is not valid format.')
      return -1
    return 0
  if len(datestr) == 10:
    datetime = datestr[:10]
    try:
      time.strptime(datetime, format)
    except:
      print('Time stamp is not valid format')
      return -1
    return 0
  if len(datestr) == 8:
    datetime = datestr[:8]
    try:
      time.strptime(datetime, format)
    except:
      print('Time stamp is not valid format')
      return -1
    return 0

def validateFailMessage(className, propertyName, reason):
  print(
    colored('Validate failed when validate instance class: ', 'red'),
    colored(className, 'green'),
    colored(' The property name is: ', 'red'),
    colored(propertyName, 'green'),
    colored(' The reason: ', 'red'),
    colored(reason, 'green')
  )

"""
!!!ATTENTION!!!
When return a validator result,
for string type, if the string is limited by strtype, return -3 if the string is
not char only, or the char is not correct format.
When the type is not correct, return -2
for over max, return 1
for less min, return -1
for pass, return 0
for the other reason not pass, return -1
"""

def ValidateString(value='', validator=None):
  if 'strtype' in validator:
    strtype = validator['strtype']
  else:
    strtype = None
  if 'minLength' in validator:
    minLength = validator['minLength']
  else:
    minLength = None
  if 'maxLength' in validator:
    maxLength = validator['maxLength']
  else:
    maxLength = None
  if minLength is not None:
    if len(value) < minLength:
      return -1
  if maxLength is not None:
    if len(value) > maxLength:
      return 1
  if strtype is not None:
    if strtype == 'uppercase' and (not value.isalpha() or not value.isupper()):
      return -3
  return 0

def ValidateDateTime(value='', validator=None):
  format = validator['format']
  if isDatetime(value, format) != 0:
    return -1
  return 0

def ValidateInteger(value, validator=None):
  if not isinstance(value, int):
    return -2
  if 'minimum' in validator:
    minimum = validator['minimum']
  else:
    minimum = None
  if 'maximum' in validator:
    maximum = validator['maximum']
  else:
    maximum = None
  if minimum is not None and value < minimum:
    return -1
  if maximum is not None and value > maximum:
    return 1
  return 0

def ValidateFloat(value, validator=None):
  if not isinstance(value, float):
    return -2
  if 'minimum' in validator:
    minimum = validator['minimum']
  else:
    minimum = None
  if 'maximum' in validator:
    maximum = validator['maximum']
  else:
    maximum = None
  if minimum is not None and value < minimum:
    return -1
  if maximum is not None and value > maximum:
    return 1
  return 0


def ValidateNumber(value, validator=None):
  if not isinstance(value, int) and not isinstance(value, float):
    return -2
  if 'minimum' in validator:
    minimum = validator['minimum']
  else:
    minimum = None
  if 'maximum' in validator:
    maximum = validator['maximum']
  else:
    maximum = None
  if minimum is not None and value < minimum:
    return -1
  if maximum is not None and value > maximum:
    return 1
  return 0

def ValidateEnum(value, validator=None):
  if 'enum' in validator:
    enum = validator['enum']
  else:
    enum = None
  if value not in enum:
    return -1
  return 0

def ValidateArray(value=None, validator=None, className=None, propertyName=None):
  passValidate = True
  itemValidateFlag = 0
  if 'minLength' in validator:
    minLength = validator['minLength']
  else:
    minLength = None
  if 'maxLength' in validator:
    maxLength = validator['maxLength']
  else:
    maxLength = None
  if 'itemValidator' in validator:
    itemValidator = validator['itemValidator']
  else:
    itemValidator = None
  if minLength is not None:
    if len(value) < minLength:
      return -1
  if maxLength is not None:
    if len(value) > maxLength:
      return 1
  if itemValidator is not None:
    try:
      for item in value:
        if itemValidator['type'] == 'string':
          itemValidateFlag = ValidateString(item, itemValidator)
          if itemValidateFlag != 0:
            raise ValidatorItemStringError
        if itemValidator['type'] == 'number':
          itemValidateFlag = ValidateNumber(item, itemValidator) 
          if itemValidateFlag != 0:
            raise ValidatorItemNumberError
        if itemValidator['type'] == 'integer':
          itemValidateFlag = ValidateInteger(item, itemValidator) 
          if itemValidateFlag != 0:
            raise ValidatorItemIntegerError
        if itemValidator['type'] == 'enum':
          itemValidateFlag = ValidateEnum(item, itemValidator)
          if itemValidateFlag != 0:
            raise ValidatorEnumError
        if itemValidator['type'] == 'object':
          if 'objectReference' in itemValidator:
            if type(item).__name__ != itemValidator['objectReference']:
              itemValidateFlag = -99
              raise ValidatorObjectError
            else:
              passValidate = Validate(item)
              if not passValidate:
                itemValidateFlag = -99
    except ValidatorObjectError:
      validateFailMessage(className, propertyName, ErrorMessage.OBJECTERROR) 
    except ValidatorItemStringError:
      if itemValidateFlag == 1:
        validateFailMessage(className, propertyName, ErrorMessage.STRINGMAXLENGTH)
      if itemValidateFlag == -1:
        validateFailMessage(className, propertyName, ErrorMessage.STRINGMINLENGTH)
      if itemValidateFlag == -3:
        validateFailMessage(className, propertyName, ErrorMessage.STRINGFORMAT)
    except ValidatorItemNumberError:
      if itemValidateFlag == -2:
        validateFailMessage(className, propertyName, ErrorMessage.ITEMNOTNUMBER)
      if itemValidateFlag == -1:
        validateFailMessage(className, propertyName, ErrorMessage.ITEMMIN)
      if itemValidateFlag == -2:
        validateFailMessage(className, propertyName, ErrorMessage.ITEMMAX)
    except ValidatorItemIntegerError:
      if itemValidateFlag == -2:
        validateFailMessage(className, propertyName, ErrorMessage.ITEMNOTINT)
      if itemValidateFlag == -1:
        validateFailMessage(className, propertyName, ErrorMessage.ITEMMIN)
      if itemValidateFlag == -2:
        validateFailMessage(className, propertyName, ErrorMessage.ITEMMAX)
    except ValidatorEnumError:
      if itemValidateFlag == -1:
        validateFailMessage(className, propertyName, ErrorMessage.ENUMERROR)
  return itemValidateFlag

def Validate(obj):
  objectClassName = obj.__class__.__name__
  rules = getattr(validateRule, objectClassName+'Rule')
  passValidate = True
  for rule in rules:
    """check each rule in the rules array"""
    propertyName = rule['name']
    propertyRequired = rule['required']
    propertyValidator = rule['validator']
    propertyValue = getattr(obj, propertyName)
    if propertyRequired:
      """This property is required."""
      try:
        if propertyValue is None or propertyValue == '':
          passValidate = False
          raise ValidatorPropertyRequiredError
      except ValidatorPropertyRequiredError:
        validateFailMessage(objectClassName, propertyName, ErrorMessage.PROPERTYREQUIRED)
    """Now we need to check the type of the validator"""
    if propertyValue is None or propertyValue == '':
      if not propertyRequired:
        pass
    if propertyValue is not None and propertyValue != '':
      validateFlag = 0
      try:
        if propertyValidator['type'] == 'string':
          validateFlag = ValidateString(propertyValue, propertyValidator)
          if validateFlag != 0:
            passValidate = False
            raise ValidatorStringError
        if propertyValidator['type'] == 'number':
          validateFlag = ValidateNumber(propertyValue, propertyValidator)
          if validateFlag != 0:
            passValidate = False
            raise ValidatorNumberError
        if propertyValidator['type'] == 'datetime':
          validateFlag = ValidateDateTime(propertyValue, propertyValidator)
          if validateFlag != 0:
            passValidate = False
            raise ValidatorTimeFormatError
        if propertyValidator['type'] == 'array':
          validateFlag = ValidateArray(propertyValue, propertyValidator, objectClassName, propertyName)
          if validateFlag != 0:
            passValidate = False
            raise ValidatorArrayError
        if propertyValidator['type'] == 'integer':
          validateFlag = ValidateInteger(propertyValue, propertyValidator)
          if validateFlag != 0:
            passValidate = False
            raise ValidatorIntegerError
        if propertyValidator['type'] == 'enum':
          validateFlag = ValidateEnum(propertyValue, propertyValidator)
          if validateFlag != 0:
            passValidate = False
            raise ValidatorEnumError
        if propertyValidator['type'] == 'object':
          if 'objectReference' in propertyValidator:
            if type(propertyValue).__name__ != propertyValidator['objectReference']:
              passValidate = False
              raise ValidatorObjectError
            else:
              if not Validate(getattr(obj,propertyName)):
                passValidate = False
      except ValidatorObjectError:
        validateFailMessage(objectClassName, propertyName, ErrorMessage.OBJECTERROR)
      except ValidatorStringError:
        if validateFlag == -1:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.STRINGMINLENGTH)
        if validateFlag == 1:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.STRINGMAXLENGTH)
        if validateFlag == -3:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.STRINGFORMAT)
      except ValidatorTimeFormatError:
        validateFailMessage(objectClassName, propertyName, ErrorMessage.STRINGDATETIMEFORMAT)
      except ValidatorArrayError:
        if validateFlag == 1:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.ARRAYMAXLENGTH)
        if validateFlag == -1:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.ARRAYMINLENGTH)
      except ValidatorIntegerError:
        if validateFlag == 1:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.INTMAX)
        if validateFlag == -1:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.INTMIN)
        if validateFlag == -2:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.NOTINT)
      except ValidatorNumberError:
        if validateFlag == 1:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.NUMBERMAX)
        if validateFlag == -1:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.NUMBERMIN)
        if validateFlag == -2:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.NOTNUMBER)
      except ValidatorEnumError:
        if validateFlag == -1:
          validateFailMessage(objectClassName, propertyName, ErrorMessage.ENUMERROR)
  return passValidate