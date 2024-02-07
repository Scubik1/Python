import re
try:
  t=int(input())
except:
  pass
else:
  if t < 1 or t > 100:
    quit()
  sets=list()
  for i in range(t):
    sets.append(input())
    if re.search(r'[^A-Z]', sets[i]):
      quit()
  answers=list()
  for set in sets:
    if len(set)==7:
      signboard=list("TINKOFF")
      for iset in range(len(set)):
        for isignboard in range(len(signboard)):
          if set[iset]==signboard[isignboard]:
            signboard.pop(isignboard)
            break
      if len(signboard)==0:
        answers.append("Yes")
      else:
        answers.append("No")
    else:
      answers.append("No")
  for answer in answers:
    print(answer)

