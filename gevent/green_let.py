from greenlet import greenlet
def test_one():
    print 'entering gr1'
    gr2.switch()
    print 'leaving gr1'

def test_two():
    print 'entering gr2'
    gr1.switch()
    print 'leaving gr2'


gr1 = greenlet(test_one)
gr2 = greenlet(test_two)


gr1.switch()
