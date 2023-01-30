# メタルハンター時限　クエスト選択状態から
import logres 

g = logres.Logres()

# メタル１
# 選択
g.gs(-227, 449)
g.gs(-140, 681)
g.gs(-141, 757, 8)

for i in range(15):
    g.gs(-453, 490, 4)
    g.gs(-134, 439, 4)

    # 戦闘
    g.gs(-80, 443, 2)
    g.click2(7)

    g.finish1()
    g.onemore(True)


