import time
import random

## 랜덤 딜레이, 1 ~ len까지
def randomDelay (len) : 
    time.sleep(random.uniform(1,len)) # delay 
    return 
    
## 고정 딜레이
def fixedDelay (len) : 
    time.sleep(len) 
    return 
