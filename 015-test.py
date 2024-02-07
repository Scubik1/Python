# TODO: реализуйте функцию encode
def encode(string):
  c=1
  out=''
  while len(string)>1:
    if string[1]==string[0]:
      if c==1:
        out=out+string[0]
        c=c+1
      else:
        c=c+1
    else:
      if c>1:
        out=out+str(c)
        c=1
      else:
        out=out+string[0] 
    string=string[1:len(string)]
  if c==1:
    out=out+string[0]
  else:
    out=out+str(c)
  return out

string = input()

print(encode(string))