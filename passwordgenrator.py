import random

s="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#abcdefghijklmnopqrstuvwxyz+=-_"

psl= 16

password = "".join(random.sample(s,psl))

print(password)

