import pyautogui as gui
import logres


lg = logres.Logres()

N = 200

for i in range(N):
    lg.gs(-165, 419, 1.526088)
    lg.gs(-305, 485, 0.528234)
    lg.gs(-120, 475, 2.698385)
    lg.gs(-132, 512, 0.644079)
    lg.gs(-438, 729, 1.594824)
    lg.gs(-360, 733, 1.448302)
    
    # 待機時間のため長め（ワンパンで倒せなかった場合)
    lg.sleep(13)
