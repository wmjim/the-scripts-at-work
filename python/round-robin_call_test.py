# 使用指南
# 1. 电脑安装 ADB 环境, ubuntu 可直接使用 sudo apt-get adb
# 2. 手机打开 USB 调试, 设置 -> 关于手机 -> 系统版本号，连续点击直到提示处于开发者模式 -> 开发人员选项 -> 打开USB调试
# 3. 手机的电话设置打开, 电源键挂断电话


from time import sleep
import os
number = 19166202108

def wait_s(t_s):
    for i in range(t_s, -1, -1):
        print("\rWait %d second" % i, end = '')
        sleep(1)
    print('')

while True:
    print("Dial number:", number)
    call = os.popen('adb shell am start -a android.intent.action.CALL -d tel:{}'.format(number))
    wait_s(8)
    print("Hang up")
    Hangup = os .popen('adb shell input keyevent 26')
    wait_s(3)
