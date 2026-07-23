from typing import TextIO, Any; from ctypes import c_void_p; import sys; 

def reverser(content): 
  if content.__class__ == str: 
    dent = [];  
    for _i in range(len(content)): 
        if content.startswith('0x', _i): 
            j = _i+2;  
            while j < len(content) and content[j].lower() in "0123456789abcdef": 
                j+=1;
                if j+1 == len(content): dent.append(content[_i:j+1])  
            if j != len(content): dent.append(content[_i:j-1]);  
    del content; 
  else: 
    dent = content.readlines(); 
    del content; 
    for _j in dent: reverser(_j); 
    return c_void_p; 
  res=""; 
  for item in dent: 
    pres=""; 
    pres += str(chr(int(item, 16))); 
    res+=pres; 
  try: print(res); del res; 
  except: return 1; 
  return 0; ## return c_void_p; 

if __name__=="__main__": 
    num = 0; 
    if sys.argv[0] == sys.argv[-1]:  
        fn: str = str(input("Enter File Name For Hex Reversion: ")); fle = open(fn, "r"); 
        while reverser(fle) != 0 and num < 5: num+=1; 
        fle.close() 
        if num != 0: print("There May Have Been An Issue During The Hex Reversion."); 
    else: ## 2nd Option To Receive Str Instead Of File 
        rec: str = input("Enter String To Reverse From Hex: "); 
        while reverser(rec) != 0 and num < 5: num+=1; 
        if num != 0: print("There May Have Been An Issue During The Hex Reversion."); 