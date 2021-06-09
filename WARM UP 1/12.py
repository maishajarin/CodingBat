def front3(str):
  if len(str) < 3:
    return str+str+str
  else:
      a= str[:3]
      return (a + a + a)


print(front3('abc'))