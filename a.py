import pyautogui as gui
import ctypes

def gs(x, y):
    gui.moveTo(x, y)
    gui.click()
    gui.sleep(3)

def gst(x, y, t=3):
    gui.moveTo(x, y)
    gui.click()
    gui.sleep(t)

#ログレスを閉じる
def offline():
    gui.moveTo(-23, 16)
    gui.click()
    gui.sleep(3)

# パソコンをスリープに
def PCsleep():
    #Windowsのスリープ
    ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)

# 終了画面
def finish():
    # スキップボタンを二回押す（安全のため）
    gst(-325, 541, 3)
    gst(-325, 541, 7)
    gst(-238, 813, 5)
    gs(-238, 813)
    gs(-238, 813)

# もう一度挑戦
def onemore():
    gst(-137, 811, 6)
    gst(-141, 752, 8)

def sleep(t=3):
    gui.sleep(3)

def click1(t=3):
    gui.moveTo(-433, 730)
    gui.click()
    gui.sleep(t)

def click2(t=3):
    gui.moveTo(-350, 730)
    gui.click()
    gui.sleep(t)

def click3(t=3):
    gui.moveTo(-261, 730)
    gui.click()
    gui.sleep(t)

def click4(t=3):
    gui.moveTo(-196, 730)
    gui.click()
    gui.sleep(t)

def click5(t=3):
    gui.moveTo(-122, 730)
    gui.click()
    gui.sleep(t)

#クエスト選択状態から
#クエスト受託
# gs(-281, 383)
# gst(-140, 756, 8)


#オシリス時限(リーフ)================
for i in range(50):
    #移動
    gst(-454, 329, 6)
    #戦闘
    gs(-121, 476)
    gst(-428, 603, 10)
    
    #終了画面 もう一度
    finish()
    onemore()


offline()
PCsleep()
#============================

#ルシェメル時限======================
# for i in range(8):
    
#     # 移動
#     gst(-7, 256, 8)
#     # 戦闘
#     gs(-88, 393)
#     click1(5)
#     click1(5)
#     click1(5)
#     click1(5)
#     click1(10)

#     finish()
#     onemore()



# 女神時限==========================
# for i in range(3):
#     # 移動
#     gst(-426, 434, 5)

#     # 戦闘
#     gs(-131, 454)
#     click4()
#     click5()
#     for j in range(2):
#         click1()
#         click2()
#         click3()
#     sleep(5)

#     #終了画面 もう一度
#     finish()
#     onemore()

# offline()
# PCsleep()

# #終了画面
    # gst(-325, 541, 10)
    # gst(-238, 813, 5)
    # gs(-238, 813)
    # gs(-238, 813)

    # # #もう一度挑戦
    # gst(-137, 811, 6)
    # gst(-141, 752, 8)

