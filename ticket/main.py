import BobTicket

if __name__ == "__main__":  # NO COVER
    a = newTicket1 = BobTicket.BobTicket("1", "finish Board")
    newTicket2 = BobTicket.BobTicket("2", "finish BackLog")
    newTicket3 = BobTicket.BobTicket("3", "finish main.py")

    a.addDescription()
    log1 = newTicket1.getLog()
    print(log1)
