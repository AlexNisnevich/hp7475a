w = plotter.write
w("SP1")

MIN, MAX = 500, 7962
pts = [(MIN, MIN), (MIN, MAX), (MAX, MAX), (MAX, MIN), (MIN, MIN)]
for i in range(40):
    x1, y1 = pts[-4][0], pts[-4][1]
    x2, y2 = pts[-5][0], pts[-5][1]   # or: x2, y2 = pts[-3][0], pts[-3][1]
    pts.append(((x1 + x2) / 2.0, (y1 + y2) / 2.0))

plotter.write(hpgl.PU(pts[0:1]))
plotter.write(hpgl.PD(pts))
plotter.write(hpgl.PU())

w("SP6")
w("PU10365,7962")
w("DI0,-1")
w(hpgl.LB(" \n\r"))

w(hpgl.LB("MIN, MAX = 500, 7962\n\r"))
w(hpgl.LB("pts = [(MIN, MIN), (MIN, MAX), (MAX, MAX), (MAX, MIN), (MIN, MIN)]\n\r"))
w(hpgl.LB("for i in range(80):\n\r"))
w(hpgl.LB("    x1, y1 = pts[-4][0], pts[-4][1]\n\r"))
w(hpgl.LB("    x2, y2 = pts[-5][0], pts[-5][1]\n\r"))
w(hpgl.LB("    pts.append(((x1 + x2) / 2.0, (y1 + y2) / 2.0))\n\r"))
w(hpgl.LB("plotter.write(hpgl.PU(pts[0:1]))\n\r"))
w(hpgl.LB("plotter.write(hpgl.PD(pts))\n\r"))
w(hpgl.LB("plotter.write(hpgl.PU())\n\r"))
