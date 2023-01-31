import pyautogui as gui
import logres 
import ctypes
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
        print("import logres\n\n", file=f)
        print("lg = logres.Logres()", file=f)



def main():

    try:
        while True:
            # 左クリック検知
            if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
                print('左クリック')
                print(gui.position())
                gui.sleep(0.5)

            # 右クリック検知
            elif ctypes.windll.user32.GetAsyncKeyState(0x02) == 0x8000:
                print("右クリック")
                gui.sleep(0.5)
        
            elif ctypes.windll.user32.GetAsyncKeyState(0x1B) == 0x8000:
                print("Escが押されました")
                break

    except KeyboardInterrupt:
        print('終了')

# main()
createFile()

