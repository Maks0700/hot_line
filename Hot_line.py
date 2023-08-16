

def define(name,father):
    
                    
                    total=""
                                  
                
                    if name.lower()=="никита":
                        
                        if father.endswith("й"):
                            if father.lower()=="юрий" or father.lower()=="василий" or father.lower()=="евгений" or father.lower()=="анатолий":
                                total=name+" "+father.replace("ий","ьевич")
                            else:
                               total=(name+" "+father.replace("й","евич"))
                        elif father=="илья":
                                total=(name+" "+father.replace("ья","ьич"))
                        elif father=="игорь":
                            total=(name+" "+father+"евич")
                        
                        else:
                                total=(f"{name} {father}ович")        
                        
                    elif name.lower()=="илья":
                        if father.endswith("й"):
                            if father.lower()=="юрий" or father.lower()=="василий" or father.lower()=="евгений" or father.lower()=="анатолий":
                                total=(name+" "+father.replace("ий","ьевич"))
                            else:
                                total=(name+" "+father.replace("й","евич"))
                        elif father=="илья":
                                total=(name+" "+father.replace("ья","ьич"))
                        elif father=="игорь":
                            total=(name+" "+father+"евич")
                        
                        else:
                                total=(f"{name} {father}ович")        
                            
                    elif name.endswith("а") or name.endswith("я"):
               
                        if father.endswith("й"):
                            if father.lower()=="юрий" or father.lower()=="василий" or father.lower()=="евгений"or father.lower()=="анатолий":
                                total=(name+" "+father.replace("ий","ьевна"))
                            else:
                                total=(name+" "+father.replace("й","евна"))
                        elif father=="илья":
                                total= (name+" "+father.replace("я","инична"))
                        elif father=="игорь":
                            total=(name+" "+father+"евна")
                        
                        else:
                                total=(name+" "+father+"овна")        
                                    
                    else:
                       
                        if father.endswith("й"):
                            if father.lower()=="юрий" or father.lower()=="василий" or father.lower()=="евгений" or father.lower()=="анатолий":
                                total=(name+" "+father.replace("ий","ьевич"))
                            else:
                                total=(name+" "+father.replace("й","евич"))
                        elif father=="илья":
                                total=(name+" "+father.replace("ья","ьич"))
                        elif father=="игорь":
                            total=(name+" "+father+"евич")
                        else:
                                total=(f"{name} {father}ович")        
                    return total














