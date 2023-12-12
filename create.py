import pyautogui as gui
import ctypes
import time
import os

# 自動クリックプログラム作成の自動化プログラム
def createFile():
    
    print("作成するpythonファイル名を入力 (.pyはなくてよい) ", end = ": ")
    fname = str(input())

    dirpath, adder = os.path.split(__file__)
    path = dirpath + "\\" + fname + ".py"

    # import文・インスタンスの記述
    with open(path, "w") as f:
        print("import pyautogui as gui", file=f)
        print("import logres\n", file=f)
        print("\nlg = logres.Logres()\n", file=f)
        print("N = 50\n", file=f) #繰り返し回数の指定
    
    return path

# 情報を書き込む
def outInf(path, xy, t):

    print(xy, end=" ")
    print("経過時間: %f" %(t))
    x, y = xy
    t = t  #遅延するか否か

    # 書き込み
    with open(path, "a") as f:
        if(REPERT):
            print("    lg.gs(%d, %d, %f)" %(x, y, t), file=f)
        else:
            print("lg.gs(%d, %d, %f)" %(x, y, t), file=f)

    return 0

# 初動タイマー
def Init():
    print("\n5秒後に計測が開始します")
    for i in range(5):
        print("%d..." %(5-i))
        time.sleep(1)
    print("start\n==6==================\n")


# 繰り返しフラグをひっくり返す
def repertToggle(path):
    global REPERT

    if(REPERT):
        print("繰り返し終了\n") 
        with open(path, "a") as f:
            print(" ", file=f)

        REPERT = False
    else:
        print("\n繰り返し開始") 
        with open(path, "a") as f:
            print("\nfor i in range(N):\n", file=f)
        
        REPERT = True

# 終了
def finish(path, settime, t):
    
    if(REPERT):
        with open(path, "a") as f:
            print("    lg.sleep(%f)" %(t), file=f)
    else:
        with open(path, "a") as f:
            print("lg.sleep(%f)" %(t), file=f)
    
    with open(path, "a") as f:
        cycle = time.time() - settime 
        print("\nlg.offline()", file=f)
        print("# lg.PCsleep()", file=f)
        print("\n# TIME : %.1f" %(cycle), file = f)
        print("# 98 minute -> N = %d" %(5880/cycle), file = f)
        print("# 58 minute -> N = %d" %(3480/cycle), file = f)

        
def main():
    global REPERT

    f = createFile()
    Init()

    # プログラム全体タイマー
    alltime = time.time()
    
    #繰り返し処理フラグ
    REPERT = False
    
    # タイマーセット
    time_sta = time.time()

    try:
        while True:
            # 左クリック
            if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
                x = gui.position()
                time_end = time.time()

                # 経過時間
                tim = time_end - time_sta
                time_sta = time.time() #初期化
                
                outInf(f, x, tim)

                gui.sleep(0.3)


            # 右クリック検知
            elif ctypes.windll.user32.GetAsyncKeyState(0x02) == 0x8000:

                repertToggle(f)
                gui.sleep(0.3)
        
            elif ctypes.windll.user32.GetAsyncKeyState(0x1B) == 0x8000:
                
                # 経過時間
                time_end = time.time()
                tim = time_end - time_sta
                time_sta = time.time() #初期化

                finish(f, alltime, tim)
                print("Escが押されました")
                break

    except KeyboardInterrupt:
        print('終了')

main()
# createFile()

