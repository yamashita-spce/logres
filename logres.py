import pyautogui as gui
import os
import ctypes

class Logres:

    #任意の場所をクリック（tで待機時間を設定)
    def gs(self, x, y, t=3):
        gui.sleep(t)
        gui.moveTo(x, y)
        gui.click()
        

    #ログレスを閉じる
    def offline(self):
        gui.moveTo(-23, 16)
        gui.click()
        gui.sleep(3)

    # パソコンをスリープに
    def PCsleep(self):
       #Windowsのスリープ
       ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)


    # 基本的な終了画面（次のクエストがない: フレンド選択なし)
    def finish1(self):
        # スキップボタンを二回押す（安全のため）
        self.gs(-325, 541, 3)
        self.gs(-325, 541, 7)
        self.gs(-238, 813, 5)
        self.gs(-238, 813)
        self.gs(-238, 813)

    # もう一度挑戦（次のクエストがない: フレンド選択なし)
    def onemore(self, friend=False):
        self.gs(-137, 811, 6)
        if(friend):
            self.gs(-141, 720)
        self.gs(-141, 752, 8)

    #待機
    def sleep(self, t=3):
        gui.sleep(t)

    def click1(self, t=3):
        gui.moveTo(-433, 730)
        gui.click()
        gui.sleep(t)

    def click2(self, t=3):
        gui.moveTo(-350, 730)
        gui.click()
        gui.sleep(t)

    def click3(self, t=3):
        gui.moveTo(-261, 730)
        gui.click()
        gui.sleep(t)

    def click4(self, t=3):
        gui.moveTo(-196, 730)
        gui.click()
        gui.sleep(t)

    def click5(self, t=3):
        gui.moveTo(-122, 730)
        gui.click()
        gui.sleep(t)

