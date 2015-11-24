def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('{}:{}'.format(sequence, result))
    return handler

handler = make_handler()

handler(1)
handler(1)
handler(1)
