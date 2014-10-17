import math
import string
Flag = 0
class Leo:
 def __init__(self, Object_view):
  if (Object_view == 'Tree')or (Object_view == 'Hunter') or (Object_view == 'Antilopa'):
   self.Object_view = Object_view
  else:
   self.Object_view = ''

 def Hungry(self):
  if self.Object_view!='':
   if self.Object_view == 'Hunter':
    return 'run'
   if self.Object_view == 'Tree':
    return 'sleep'
   if self.Object_view == 'Antilopa':
    Flag = 2
    return 'eat, full'
  else:
   return 'Lion can not see this object!'

 def Full(self):
    if self.Object_view!='':
        if self.Object_view == 'Hunter':
            iFlag = 1
            return 'run, hungry'
        if self.Object_view == 'Tree':
            iFlag = 1
            return 'look, hungry'
        if self.Object_view == 'Antilopa':
           iFlag = 1
           return 'sleep, hungry'
    else:
       return 'Lion can not see this object!'

#rp = Leo (0)
#print rp.Full()


