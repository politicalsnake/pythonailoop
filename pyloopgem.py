# It is VERY BUGGY

from google import genai
import subprocess
from google.genai import types

the = True
go = True
ct = 0
cd = "yolo"
td = "yele"
gg = 0
print("Enter gemini API key:")
key = input()
print("You need at least 3 tokens to work. You start with 15. If you run out, code will stop.")

while the == True:
    cd = "yolo"
    td = "yele"
    gg = 0
    tg = 0
    client = genai.Client(api_key=key)
    print("Enter input:")
    query = input()
    print("Your input was: ",query," would you like to revise?")
    yn = input()
    if yn == "yes":
        continue
    response = client.models.generate_content(model = "gemini-2.0-flash",
                                              contents = (query,"WRITE ONLY THE PROGRAM IN PYTHON. WRITE NOTHING ELSE."), 
                                              config = types.GenerateContentConfig(temperature = 0))
    ct = ct + 1
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
    ct = ct + 1
    while go == True:
        gg = gg + 1
        tg = tg + 1
        print("revision number:",gg)
        print("tokens used:",ct)
        cd = coderevis.text
        td = coderevis.text
        print(cd)
        if ct == 15:
            go = False
            the = False
            print("You have run out of queries. Restart program for more.")
            break
        if "yes" not in cd and gg == 1:
            with open("script.py","w") as f:
                f.write(thecode)
            res = subprocess.run(['python','script.py'], capture_output = True, text = True)
            coderevis = client.models.generate_content(model = "gemini-2.0-flash",
                                         contents = ("The function the code to write should be:",query,"the code is:",cd,"The output of the code was",res.stdout,"Is this acceptable? If acceptable, type yes and nothing else. If unnaceptable, type revised code."),
                                         config = types.GenerateContentConfig(temperature = 1))
            ct = ct + 1
            if "yes" in coderevis.text:
                td = coderevis.text
            else:
                cd = coderevis.text
                td = coderevis.text
            td = coderevis.text
            print("Revised code or yes, it works:",td)
            print("Out:",res.stdout)
        if "yes" not in cd and gg > 1:
            with open("script.py","w") as f:
                f.write(coderevis.text)
            res = subprocess.run(['python','script.py'], capture_output = True, text = True)
            coderevis = client.models.generate_content(model = "gemini-2.0-flash",
                                         contents = ("The function the code to write should be:",query,"the code is:",cd,"The output of the code was",res.stdout,"Is this acceptable? If acceptable, type yes and nothing else. If unnaceptable, type a revised script."),
                                         config = types.GenerateContentConfig(temperature = 1))
            ct = ct + 1
            if "yes" in coderevis.text:
                td = coderevis.text
            else:
                cd = coderevis.text
                td = coderevis.text
            td = coderevis.text
            print("Revised code or yes, it works:",td)
            print("Revised code or original:",cd)
            print("Out:",res.stdout)
        if "yes" in td:
            if tg == 1:
                print("countfirst")
                print(" ")
                with open("script.py","w") as f:
                     f.write(thecode)
                res = subprocess.run(['python','script.py'], capture_output = True, text = True)
                print("Final output:")
                print(res.stdout)
                print("Final code:")
                print(thecode)
                if ct < 12:
                    print("Query count:",ct)
                    print("You have enough tokens. Code starting over.")
                    break
                elif ct > 12:
                    print("Query count:",ct)
                    print("You do not have enough tokens. Code ending.")
                    go = False
                    the = False
                    break
                break
            elif tg > 1:
                print("countafter")
                print(" ")
                print("Final output:")
                print(res.stdout)
                print("Final code:")
                print(cd)
                if ct < 12:
                    print("Query count:",ct)
                    print("You have enough tokens. Code starting over.")
                    break
                elif ct > 12:
                    print("Query count:",ct)
                    print("You do not have enough tokens. Code ending.")
                    go = False
                    the = False
                    break
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
            ct = ct + 1