
import sys
def str_to_dpid ( s ):
  
  if s.lower().startswith("0x"):
    s = s[2:]
  s = s.replace("-", "").split("|", 2)
  a = int(s[0], 16)
  if a > 0xffFFffFFffFF:
    b = a >> 48
    a &= 0xffFFffFFffFF
  else:
    b = 0
  if len(s) == 2:
    b = int(s[1])
  return a | (b << 48)
#strToDPID = str_to_dpid
print str_to_dpid("0000000000000201")