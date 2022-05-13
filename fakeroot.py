import os, sys
os.system('pkg install proot')
os.system('clear')
print("""
  ______    _        _____             _   
 |  ____|  | |      |  __ \           | |  
 | |__ __ _| | _____| |__) |___   ___ | |_ 
 |  __/ _` | |/ / _ \\  _  // _ \ / _ \\| __|
 | | | (_| |   <  __/ | \\ \\ (_) | (_) | |_ 
 |_|  \\__,_|_|\\_\\___|_|  \\_\\___/ \\___/ \__|""")                 
print('\n---Created by Aceinet---\nTo install packages first exit the root\n-----------\nRoot switched on ✓')

os.system('proot -0 -w ~ $PREFIX/bin/bash')
os.system('clear')
print('FakeRoot: Exited')