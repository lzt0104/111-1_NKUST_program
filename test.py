while True: 
    try: 
       n = int(input()) 
       summer = 0 
       nonsummer = 0 
       if n>700: 
           summer += ((n-700)*5.63) 
           nonsummer += ((n-700)*4.5) 
           n = 700 
       if n>500: 
           summer +=((n-500)*4.97) 
           nonsummer += ((n-500)*4.01) 
           n = 500 
       if n>330: 
           summer += ((n-330)*4.39) 
           nonsummer += ((n-330)*3.61) 
           n = 330 
       if n>120: 
           summer += ((n-120)*3.02) 
           nonsummer += ((n-120)*2.68) 
           n = 120 
       if n > 0: 
           summer += (n*2.1) 
           nonsummer += (n*2.1) 
       print("Summer months:{}".format(format(summer,'.2f'))) 
       print("Non-Summer months:{}".format(format(nonsummer,'.2f'))) 
    except: 
        break  