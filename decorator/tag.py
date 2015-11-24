#import ipdb
#ipdb.set_trace()

# decorator chain execute from top to bottom
# return from bottom to top

def makebold(fn):
    def wrapped():
        print 'first printed'
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        print 'second printed'
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
        return "hello world"


print hello() ## returns <b><i>hello world</i></b>
