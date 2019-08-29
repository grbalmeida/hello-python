from sales.formatting.real import real

def increase(value, percentage, formats=False):
  value = value + (value * (percentage / 100))

  if formats:
    return real(value)
  
  return value

def decrease(value, percentage, formats=False):
  value = value - (value * (percentage / 100))

  if formats:
    return real(value)
  
  return value
