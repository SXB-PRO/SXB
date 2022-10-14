import platform
bit=platform.architecture()[0]
if bit =='64bit':
    import SXB
    SXB.main_apv()
else:
    print('Sorry device or system not support this tools')
    exit()
