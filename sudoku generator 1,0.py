# Sudoku generator
# 0.6 16-05-2018
# Matthew Doe
# row = line of 9 unique integers [1..9], square = 3x3 box of 9 unique integers, column = stack of 9 unique integers

def sudoku(dif = 0, size = 0): #dif in range 0(none) to 2(easy) - 6(medium) - 8(hard)
    import time
    start = time.clock()
    import random
    n=0
    nset = range(1,10)                                          # number set of 9 [1..9]
    chain = [0,1,2,3,4,5,6,7,8]                                 # identifier for individual nset, conflict with range approach
    fuq = 0 #iteration catcher with approriate name..

    q = (random.sample([1,2],1)[0])

# 9x9 block builder
    while n < 9:                                                # !!! Just to generate the first 6 chains?
        if n==0:                                                #lay base first row
            chain[n] = random.sample(nset, len(nset))           #randomizer [1..9]
            print('...generating your sudoku...')               #signal as intermitant operational test, !!! to be moved down script...
            n = n+1

        elif n==1 or n==2:                                      #check against previous row(s) in the respective square  
            chain[n] = [0,0,0,0,0,0,0,0,0]
            # generate square compatibility
            if q==1: #BCA
                chain[n][0:3] = random.sample(chain[0][3:6], 3)
                chain[n][3:6] = random.sample(chain[0][6:9], 3)
                chain[n][6:9] = random.sample(chain[0][0:3], 3)
            else: #CAB
                chain[n][0:3] = random.sample(chain[0][6:9], 3)
                chain[n][3:6] = random.sample(chain[0][0:3], 3)
                chain[n][6:9] = random.sample(chain[0][3:6], 3)
                

            n = n+1
            if n==2:
                q=int(1 / (q / 2))                              #Bit flip..

        elif n in [3,4,5]:
            chain[n] = [0,0,0,0,0,0,0,0,0]
            m = 0
            x = [0,0,0,0,0,0]
            while m < 9:
                if m==0 or m==3 or m==6:                        #vertical ABC-BCA-CAB source set selection
                    x = [chain[0][m+1], chain[1][m+1], chain[2][m+1], chain[0][m+2], chain[1][m+2], chain[2][m+2]]
                    chain[n][m]= (random.sample(x,1)[0])
                    if (chain[n][m] in chain[n][0:m]):      #check on row compatibiluty
                        fuq = fuq+1
                        m=0
                    elif n==4 and (chain[n][m] in chain[n-1][m:m+3]): #includes check on square compatiblity
                        fuq = fuq+1
                        m=m
                    elif n==5 and ((chain[n][m] in chain[n-1][m:m+3]) or (chain[n][m] in chain[n-2][m:m+3])):
                        fuq = fuq+1
                        m=m
                    else:
                        m=m+1
                elif m==1 or m==4 or m==7:
                    x = [chain[0][m-1], chain[1][m-1], chain[2][m-1], chain[0][m+1], chain[1][m+1], chain[2][m+1]]
                    chain[n][m]= (random.sample(x,1)[0])
                    if (chain[n][m] in chain[n][0:m]):      #check on row compatibiluty
                        fuq = fuq+1
                        m=0
                    elif n==4 and (chain[n][m] in chain[n-1][(m-1):(m+2)]): #includes check on square compatiblity
                        fuq = fuq+1
                        m=(m-1)
                    elif n==5 and ((chain[n][m] in chain[n-1][(m-1):(m+2)]) or (chain[n][m] in chain[n-2][(m-1):(m+2)])): #includes check on column compatiblity
                        fuq = fuq+1
                        m=(m-1)
                    else:
                        m=m+1
                elif m==2 or m==5 or m==8:
                    x = [chain[0][m-2], chain[1][m-2], chain[2][m-2], chain[0][m-1], chain[1][m-1], chain[2][m-1]]
                    chain[n][m]= (random.sample(x,1)[0])
                    if (chain[n][m] in chain[n][0:m]):      #check on row compatibiluty
                        fuq = fuq+1
                        m=0
                    elif n==4 and (chain[n][m] in chain[n-1][(m-2):(m+1)]): #includes check on square compatiblity
                        fuq = fuq+1
                        m=(m-2)
                    elif n==5 and ((chain[n][m] in chain[n-1][(m-2):(m+1)]) or (chain[n][m] in chain[n-2][(m-2):(m+1)])): #includes check on column compatiblity
                        fuq = fuq+1
                        m=(m-2)
                    else:
                        m=m+1
                    
                if fuq > 1250000:
                    m = m+1
                    print("iteration crash on unselectable number")
                    print(chain[n])
                    end = time.clock()
                    print(str(end-start)+" seconds" )
                    return

            n = n+1

        elif n in [6,7,8]:
            chain[n] = [0,0,0,0,0,0,0,0,0]
            m = 0
            if n ==6: print()
            while m < 9:
                z = [1,2,3,4,5,6,7,8,9]
                for i in range(6):
                    z.remove(chain[i][m])
                    
                if m < 3: l=0
                elif m <6: l=3
                else: l=6
                fuq=0
                chain[n][m] = (random.sample(z,1)[0])
                if (chain[n][m] in chain[n][0:m]):      #check on row compatibiluty
                    fuq = fuq+1
                    m=0
                elif n==7 and (chain[n][m] in chain[n-1][l:l+3]): #includes check on square compatiblity
                    fuq = fuq+1
                    m=m
                elif n==8 and ((chain[n][m] in chain[n-1][l:l+3]) or (chain[n][m] in chain[n-2][l:l+3])):
                    fuq = fuq+1
                    m=m
                else:
                    m=m+1
                if fuq > 1000000:
                    m = m+1
                    print("iteration crash on unselectable number")
                    print(chain[n])
                    end = time.clock()
                    print(str(end-start)+" seconds" )
                    return   
            n=n+1

# Check multiple solutions within sudoku, specifically interchangable number sets
    store = chain #Storage of complete sudoku
    mid = time.clock()
    print(str(mid-start)+" seconds" )
    h = 0
    o = 0
    p = 0
    pairs = [0,0,0,0,0,0,0,0,0,0,0,0]
    while h < 8:
        for i in range(8):    #horizontal, last column doesnt need to be checked
            while o < 9:
                if chain[h][i] == chain[h+1][o] and chain[h+1][i] == chain[h][o]:
                    pairs[p] = [[h,i],[h,o],[h+1,i],[h+1,o]]
                    if (p>0 and [h,i] in pairs[p-1]) or (p>1 and [h,i] in pairs[p-2]):
                        p = p
                        pairs[p]=0
                    else: p = p+1
                o = o+1
            o =0
        if h == 1 or h == 4:  
            h = h+2
        else:
            h = h+1

    h=0
    while h < 8:        
        for i in range(8):    #vertical, last column doesnt need to be checked
            while o < 9:
                if chain[i][h] == chain[o][h+1] and chain[i][h+1] == chain[o][h]:
                    pairs[p]: pairs[p] = [[i,h],[i,h+1],[o,h],[o,h+1]]
                    if (p>0 and [i,h] in pairs[p-1]) or (p>1 and [i,h] in pairs[p-2]):
                        p = p
                        pairs[p]=0
                    else: p = p+1
                o = o+1
            o = 0
        if h == 1 or h == 4:  
            h = h+2
        else:
            h = h+1
    print(pairs)
    
# Number eliminator for sudoku generator...
    score = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(dif*24):
        o = (random.sample(range(9),1)[0])
        p = (random.sample(range(9),1)[0])
        for m in range((12-len([1 for x in pairs if x==0]))):
            if ([o,p] in pairs[m] and score[m]<4):
                score[m]=score[m]+1
            else:
                score[m]=score[m]+1
                chain[o][p]=' '

    for n in range(9):
        st =('|'+' '+str(chain[n][0])+' '+str(chain[n][1])+' '+str(chain[n][2])+' '+'|'+' '+str(chain[n][3])+' '+str(chain[n][4])+' '+str(chain[n][5])+' '+'|'+' '+str(chain[n][6])+' '+str(chain[n][7])+' '+str(chain[n][8])+' '+'|')  #
        print(st)
        if n==2 or n==5:
            st = '_'*len(st)
            print(st)
    end = time.clock()
    print()
    print(str(end-start)+" seconds" )
    return              
#end
