def get_fractions(frac_str):
    """
    Funcion "get_fractions" cuya finalidad es convertir un numero en formato "str" a "float".
    tambien, ubica espacialmente los "/" si la variable "frac_str" es fraccion y almacena un numero en formato "str".  

    Parameters
    ----------
    frac_str : Numero que puede ser int, float o str.
        

    Returns
    -------
    En primera instancia, devuelve el numero en int o float si no es formato str.
    Si el numero es str, se devuelve convertido exitosamente a float, ya sea entero o decimal. 
    """
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

def suma(a, b):
    """
    Funcion que permite la suma de dos numeros reales.

    Parameters
    ----------
    a : Numero entero o decimal en formato int o float.
        
    b : Numero entero o decimal en formato int o float.
        

    Returns
    -------
    Devuelve la suma de las variables sumando_a y el sumando_b.
    """
  sumando_a = get_fractions(a)
  sumando_b = get_fractions(b)
  return sumando_a + sumando_b

def multiplica(a, b):
    """
    Funcion que realiza el producto de dos numeros reales.

    Parameters
    ----------
    a : Numero entero o decimal en formato int o float.
        
    b : Numero entero o decimal en formato int o float.
        

    Returns
    -------
    Devuelve el producto de las variables multiplicando y multiplicador.
    """
  multiplicando = get_fractions(a)
  multiplicador = get_fractions(b)
  return multiplicando * multiplicador

