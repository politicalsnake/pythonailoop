# It is VERY BUGGY

from google import genai
import subprocess
from google.genai import types

the = True
go = True
ct = 0
cd = "yolo"
td = "yele"

while the == True:
    client = genai.Client(api_key="")
    print("Enter input:")
    query = input()
    print("Your input was: ",query," would you like to revise?")
    yn = input()
    if yn == "yes":
        continue
    response = client.models.generate_content(model = "gemini-2.0-flash",
                                              contents = (query,"WRITE ONLY THE PROGRAM IN PYTHON. WRITE NOTHING ELSE."), 
                                              config = types.GenerateContentConfig(temperature = 0))
    code = response.text
    code = code.replace("```python","")
    code = code.replace("```","")
    print("Initial program:")
    print(code)
    thecode = code
    with open("script.py","w") as f:
        f.write(code)
    res = subprocess.run(['python','script.py'], capture_output = True, text = True)
    print("Initial output:")
    print(res.stdout)
    coderevis = client.models.generate_content(model = "gemini-2.0-flash",
                                         contents = ("Your last input was",query,"WRITE ONLY THE PROGRAM IN PYTHON. WRITE NOTHING ELSE. The output of the code you wrote for this query was",res.stdout,"Is this acceptable? If acceptable, type yes and nothing else. If unnaceptable, type revised code."), 
                                         config = types.GenerateContentConfig(temperature = 0))
    while go == True:
        cd = coderevis.text
        td = coderevis.text
        print(cd)
        ct = ct + 1
        if ct == 15:
            print("eee")
            break
        print(ct)
        if "yes" not in cd:
            print("eeee")
            with open("script.py","w") as f:
                f.write(coderevis.text)
            res = subprocess.run(['python','script.py'], capture_output = True, text = True)
            coderevis = client.models.generate_content(model = "gemini-2.0-flash",
                                         contents = ("The function the code to write should be:",query,"the code is:",cd,"The output of the code was",res.stdout,"Is this acceptable? If acceptable, type yes and nothing else. If unnaceptable, type revised code."),
                                         config = types.GenerateContentConfig(temperature = 1))
            if "yes" in coderevis.text:
                td = coderevis.text
            else:
                cd = coderevis.text
                td = coderevis.text
            td = coderevis.text
            print(td,"t")
            print(cd,"c")
            print(res.stdout)
        if "yes" in td:
            if ct == 1:
                with open("script.py","w") as f:
                     f.write(thecode)
                res = subprocess.run(['python','script.py'], capture_output = True, text = True)
                print("final output:")
                print(res.stdout)
                print("final code:")
                print(thecode)
                go = False
                the = False
                break
            elif ct > 1:
                print("final code:")
                print(cd)
                print("final output:")
                print(res.stdout)
                go = False
                the = False
                break
        print("Interrupt revision process and send message to Gemini?")
        ny = input()
        if ny == "yes":
            cd = coderevis.text
            print("please say only what is wrong with the code.")
            rev = input()
            coderevis = client.models.generate_content(model = "gemini-2.0-flash",
                                     contents = ("I wrote this program:",cd,"It is buggy. The output is.",res.stdout, "Please revise with this advice:",rev),
                                     config = types.GenerateContentConfig(temperature = 1))
            print("uhu")
            ct = ct + 1
    
    
