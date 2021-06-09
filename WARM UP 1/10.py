def pos_neg(a, b, negative):
  if negative == True and a<0 and b<0:
    return True
  elif a>0 and b<0 and negative== False:
    return True
  elif a<0 and b>0 and negative== False:
    return True
  else: return False