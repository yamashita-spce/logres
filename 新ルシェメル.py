import pyautogui as gui
import logres


lg = logres.Logres()

N = 36


for i in range(N):
    lg.gs(-80, 270, 1.742290)
    lg.gs(-74, 393, 7.022599)
    lg.gs(-75, 397, 0.556538)
    lg.gs(-75, 400, 1.310537)
    lg.gs(-427, 721, 0.860460)
    lg.gs(-415, 726, 3.668984)
    lg.gs(-423, 717, 6.194169)
    lg.gs(-433, 726, 5.040450)
    lg.gs(-425, 719, 4.336177)
    lg.gs(-321, 547, 12.358792)
    lg.gs(-321, 547, 1.016727)
    lg.gs(-237, 812, 7.553621)
    lg.gs(-231, 815, 5.088164)
    lg.gs(-234, 812, 3.692029)
    lg.gs(-141, 807, 2.394836)
    lg.gs(-138, 756, 5.599288)
    lg.sleep(8.159379)

lg.offline()
# lg.PCsleep()

# TIME : 76.6
# 98 minute -> N = 76
