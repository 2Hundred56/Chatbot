def output(msg):
    print(msg)
def loop(input_func):
    run=1
    while run:
        msg_input=raw_input("> ")
        if msg_input.upper()=="QUIT":
            run=0
        else:
            input_func(msg_input)
