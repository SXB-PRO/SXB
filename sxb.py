import platform
bit=platform.architecture()[0]
if bit =='64bit':
    import SXB
   SXB.subscription
else:
    print('Sorry device or system not support this tools')
    exit()
