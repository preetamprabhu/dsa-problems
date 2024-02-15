class hash_mapsandsets:

    # leitrally dictionary 
    # hashmap

    hm={}
    hm['a']=2
    hm['b']=3
    hm['c']=4
    hm['d']=5
    print(hm)



    # changes the value of the key 'a' from 2 to 7

    hm['a']=7
    print(hm)


    # adds another key 'k' to the hm{} with value 99

    hm['t']=7
    print(hm)
    # same named multiple keys are not possible,but same values can be given to different keys

    #delete a key and value 

    del hm['b']
    print(hm)


    # -----------------------------------------------------------------------


    # hash sets

    # literally set


    # set is implemented by a variable[     a=set() and added using a.add()   ] we het o/p in terms of{'c','b'}

    hs=set()
    hs.add(1)
    hs.add('hello')
    print(hs)

    # to remove the elements in set you have to give the value of 

    hs.remove(1)
    print(hs)

    print(hs.__contains__(2))      #checks for the element "2" if not there returns false


