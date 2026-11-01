if __name__=="__main__":
    ppl=list(range(1, 234))
    idx=0
    while len(ppl)>1:
        idx=(idx+2)%len(ppl)
        ppl.pop(idx)
    print("最後剩下的是原來的第", ppl[0], "個")