import platform
bit=platform.architecture()[0]
if bit =='64bit':
    import sxb.py
   sxb.py.subscription
else:
    print('Sorry device or system not support this tools')
    exit()
