def hi():
    d1 >> play(P['AAJBAS'].bubble())
    d2 >> play(P['JOSS'].amen())
    d3 >> play('good afternoon')
    p3 >> rave()
    Clock.future(12, hi)
hi()

def pyohio_is_fun():
    p1 >> bell([0, 8, 2])
    p2 >> dbass([-2, 3, 6])
    p4 >> arpy()
    Clock.future(9, pyohio_is_fun)
pyohio_is_fun()

def thanks_for_having_me():
    p5 >> zap()
    s1 >> loop('/Users/jessicagarson/Documents/we_are_the_one.wav', dur=9)
    Clock.future(15, thanks_for_having_me)
thanks_for_having_me()
