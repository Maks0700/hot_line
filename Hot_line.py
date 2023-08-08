#The topic----the modules of Python 



exc_name=["Василий","Игорь","Андрей","Сергей","Матвей","Евгений","Дмитрий","Юрий","Алексей"]
while True:
    name=input("Введите ваше имя: ")
    father=input("Введите имя отца: ")
 #мужики   
    
    if name.lower()=="никита":
        
        if father.lower()=="юрий" or father.lower()=="василий" or father.lower()=="евгений" or father.lower()=="анатолий":
                print(name+" "+father.replace("ий","ьевич"))
        elif father=="илья":
                 print(name+" "+father.replace("ья","ич"))
        else:
                print(name+" "+father.replace("й","евич"))
    else:
                print(f"{name} {father}ович")        
        
    elif name.lower()=="илья":
        if father.endswith("й"):
            if father.lower()=="юрий" or father.lower()=="василий" or father.lower()=="евгений" or father.lower()=="анатолий":
                print(name+" "+father.replace("ий","ьевич"))
            elif father=="илья":
                 print(name+" "+father.replace("ья","ич"))
            else:
                print(name+" "+father.replace("й","евич"))
        else:
                print(f"{name} {father}ович")        
            
    
    
    
    
    
    
    elif name.endswith("а") or name.endswith("я"):
#телки
         if father.endswith("й"):
            if father.lower()=="юрий" or father.lower()=="василий" or father.lower()=="евгений"or father.lower()=="анатолий":
                print(name+" "+father.replace("ий","ьевна"))
            else:
                print(name+" "+father.replace("й","евна"))
         elif father=="илья":
                print(name+" "+father.replace("я","инична"))
         
         else:
                print(name+" "+father.replace("а","овна"))        
                    
    else:
#мужики без никиты и ильи        
        if father.endswith("й"):
            if father.lower()=="юрий" or father.lower()=="василий" or father.lower()=="евгений" or father.lower()=="анатолий":
                print(name+" "+father.replace("ий","ьевич"))
            
            elif father=="илья":
                 print(name+" "+father.replace("ья","ич"))
            else:
                print(name+" "+father.replace("й","евич"))
        else:
                print(f"{name} {father}ович")        
           









