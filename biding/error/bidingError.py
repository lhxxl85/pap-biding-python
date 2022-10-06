class ValidatorPropertyRequiredError(Exception):
  """According to the rule, this field is required."""
  pass

class ValidatorStringError(Exception):
  """According to the rule, the string is failed"""
  pass

class ValidatorTimeFormatError(Exception):
  """According to the rule, the string is not date time format"""
  pass

class ValidatorArrayError(Exception):
  """According to the rule, the array length is not in the limit range"""
  pass

class ValidatorItemStringError(Exception):
  """According to the rule, the string item in the array is failed"""
  pass

class ValidatorItemNumberError(Exception):
  """According to the rule, the number item in the array is failed"""
  pass

class ValidatorItemIntegerError(Exception):
  """According to the rule, the integer item in the array is failed"""
  pass

class ValidatorIntegerError(Exception):
  pass

class ValidatorNumberError(Exception):
  pass

class ValidatorEnumError(Exception):
  pass

class ValidatorObjectError(Exception):
  pass

class ErrorMessage:
  PROPERTYREQUIRED = 'The value of this property can not be None or \'\''
  ITEMSTRINGMAXLENGTH = 'The item string length has exceeded the limit.'
  ITEMSTRINGMINLENGTH = 'The item string length must be more then the limit'
  STRINGMAXLENGTH = 'The string length has exceeded the limit.'
  STRINGMINLENGTH = 'The string length must be more then the limit'
  STRINGDATETIMEFORMAT = 'The string is not a datetime format.'
  ARRAYMAXLENGTH = 'The array length has exceeded the limit.'
  ARRAYMINLENGTH = 'The array length must be more then the limit.'
  ITEMNOTNUMBER = 'The item in the array is not a number.'
  ITEMMIN = 'The item value must be more then the limit.'
  ITEMMAX = 'The item value has exceeded the limit'
  ITEMNOTINT = 'The item in the array is not a integer.'
  INTMAX = 'The integer has exceeded the limit.'
  INTMIN = 'The integer must be more then the limit.'
  NUMBERMAX = 'The number has exceeded the limit.'
  NUMBERMIN = 'The number must be more then the limit.'
  NOTINT = 'The type of this property is not a int.'
  NOTNUMBER = 'The type of this property is not a number.'
  STRINGFORMAT = 'The string is not correct format.'
  ENUMERROR = 'The string is not a enum member.'
  OBJECTERROR = 'The object is not match with the requirement.'