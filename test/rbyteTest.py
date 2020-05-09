import time

str = '\r*'
file_full_name = 'a.jpg'
done_block = 0

for i in range(50):
    done_block += 1
    now_jd = done_block * 2
    print("\r %s" % (i * '*'), end='')
    print("\r %s：[%s%s] %d%% " % (file_full_name, done_block * '█', ' ' * (50 - done_block), now_jd), end="")
    time.sleep(0.2)