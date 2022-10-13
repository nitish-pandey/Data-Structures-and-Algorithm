
rom=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
nums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]

def romanss_to_int(s):
    global rom,nums

    rom_num=0

    
    

def int_to_roman(number):

    global rom,nums

    rom_num=''

    i=0

    while number>0 and i<13:

        div=number//nums[i]
        number=number%nums[i]

        rom_num+=rom[i]*div

        i+=1



    return rom_num


n=400

r=int_to_roman(n)
print(r)

a=romanss_to_int(r)
print(a)

