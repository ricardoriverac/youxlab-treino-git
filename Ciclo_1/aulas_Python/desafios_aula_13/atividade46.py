import time 
print('\033[1;33mFuja, uma bomba vai explodir em 10 segundos!!\033[m')
time.sleep(1)
for c in range (10, -1, -1):
    print(c)
    time.sleep(1)
print('\033[1;31mBUM!  BUM!  POOOW\033m')