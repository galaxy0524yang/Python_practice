# '+=' & 'join()' の実行するには必要な時間テスト

import time

time01 = time.time()        #start time

time
a = ""

for i in range(100000000):
    a += "sxt"

time02 = time.time()        #end time
print("完了まで、"+str(time02-time01)+"秒かかりました。")


time03 = time.time()        #start time

li = []
for i in range(100000000):
    li.append("sxt")

a = "".join(li)

time04 = time.time()        #end time

print("完了まで、"+str(time04-time03)+"秒かかりました。")