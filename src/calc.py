def get_fractions(frac_str):
  if isinstance(frac_str, int) or isinstance(frac_str, float):
    return frac_str

  if("/" in frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac
  else:
    return float(frac_str)
