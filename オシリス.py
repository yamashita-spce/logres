import pyautogui as gui
import logres


lg = logres.Logres()

N = 50


for i in range(N):
    lg.gs(-461, 340, 1.250084)
    lg.gs(-136, 479, 5.657024)
    lg.gs(-131, 480, 1.477272)
    lg.gs(-422, 731, 1.329089)
    lg.gs(-309, 545, 11.132085)
    lg.gs(-335, 543, 0.801363)
    lg.gs(-318, 544, 2.581406)
    lg.gs(-229, 816, 7.747649)
    lg.gs(-223, 815, 6.422369)
    lg.gs(-232, 817, 5.633469)
    lg.gs(-111, 816, 2.370121)
    lg.gs(-145, 756, 5.300889)
    lg.sleep(8)

lg.offline()
# lg.PCsleep()
