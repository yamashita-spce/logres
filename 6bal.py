import pyautogui as gui
import logres


lg = logres.Logres()

N = 60


for i in range(N):

    lg.gs(-241, 389, 2.436321)
    lg.gs(-239, 509, 1.603369)
    lg.gs(-232, 475, 1.264287)
    lg.gs(-107, 440, 2.462657)
    lg.gs(-273, 734, 4.499757)
    lg.gs(-118, 740, 0.910809)
    lg.gs(-415, 648, 3.172258)
    lg.gs(-207, 734, 2.969081)
    lg.gs(-428, 729, 1.022983)
    lg.gs(-201, 731, 21.716982)
    lg.gs(-355, 732, 1.286896)
    lg.gs(-269, 733, 11.506752)
    lg.gs(-201, 733, 3.288334)
    lg.gs(-425, 644, 13.764268)
    lg.gs(-350, 730, 1)
    gui.sleep(25)
 
lg.offline()
lg.PCsleep()