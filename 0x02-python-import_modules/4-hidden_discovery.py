#!/usr/bin/python3.8

if __name__ == "__main__":

    import hidden_4

    fil = dir(hidden_4)
    for i in range(len(fil)):
        if (fil[i][0] != "_"):
            print(fil[i])
