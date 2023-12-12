import pyautogui as gui
import logres


lg = logres.Logres()

N = 127

for i in range(N):

    lg.gs(-242, 400, 1.448938)
    lg.gs(-215, 525, 0.872502)
    lg.gs(-234, 480, 0.870288)
    lg.gs(-84, 437, 1.739149)
    lg.gs(-84, 440, 0.448754)
    lg.gs(-123, 734, 1.486885)
    lg.gs(-421, 740, 1.121354)
    lg.gs(-352, 732, 0.348916)
    lg.gs(-272, 731, 0.523799)
    lg.gs(-178, 737, 0.561804)
    lg.gs(-347, 747, 14.028744)
    lg.gs(-435, 642, 1.123473)
    lg.sleep(20.654062)

lg.offline()
lg.PCsleep()

# TIME : 45.2
# 98 minute -> N = 127
