# It is VERY BUGGY

from google import genai
import subprocess
from google.genai import types

the = True
go = True
ct = 0
cd = "yolo"

while the == True:
    client = genai.Client(api_key="AIzaSyAUiqd8mnnguM_opAUE1r-YcC1_nwtJ-As")
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
        ct = ct + 1
        if ct == 15:
            break
        print(ct)
        if "yes" not in cd:
            with open("script.py","w") as f:
                f.write(coderevis.text)
            res = subprocess.run(['python','script.py'], capture_output = True, text = True)
            coderevis = client.models.generate_content(model = "gemini-2.0-flash",
                                         contents = ("The function the code to write should be:",query,"the code is:",cd,"The output of the code was",res.stdout,"Is this acceptable? If acceptable, type yes and nothing else. If unnaceptable, type revised code."),
                                         config = types.GenerateContentConfig(temperature = 1))
            td = coderevis.text
            print(td)
            print(res.stdout)
            if "yes" in td:
                the = False
                go = False
                if ct == 1:
                    with open("script.py","w") as f:
                         f.write(thecode)
                    res = subprocess.run(['python','script.py'], capture_output = True, text = True)
                    print("final output:")
                    print(res.stdout)
                    print("final code:")
                    print(thecode)
                elif ct > 1:
                    print("final code:")
                    print(cd)
                    print("final output:")
                    print(res.stdout)
                break
            ny = input()
            print("Interrupt revision process and send message to Gemini?")
            if ny == "yes":
                cd = coderevis.text
                print("please say only what is wrong with the code.")
                rev = input()
                coderevis = client.models.generate_content(model = "gemini-2.0-flash",
                                         contents = ("I wrote this program:",cd,"It is buggy. The output is.",res.stdout, "Please revise with this advice:",rev),
                                         config = types.GenerateContentConfig(temperature = 1))
                ct = ct + 1
    
    
