# It is VERY BUGGY

from google import genai
import subprocess
from google.genai import types

the = True
go = True
ct = 0

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
    print("")
    print(code)
    with open("script.py","w") as f:
        f.write(code)
    res = subprocess.run(['python','script.py'], capture_output = True, text = True)
    coderevis = client.models.generate_content(model = "gemini-2.0-flash",
                                         contents = ("Your last input was",query,"WRITE ONLY THE PROGRAM IN PYTHON. WRITE NOTHING ELSE. The output of the code you wrote for this query was",res.stdout,"Is this acceptable? If acceptable, type yes and nothing else. If unnaceptable, type revised code."), 
                                         config = types.GenerateContentConfig(temperature = 0))
    while go == True:
        ct = ct + 1
        if ct == 15:
            go == False
        print(ct)
        if "yes" in coderevis.text:
            print("Out:")
            print(res.stdout)
            print("Final response:")
            print("")
            print(coderevis.text)
            print("program completed.")
            the = False
            go = False
        else:
            with open("script.py","w") as f:
                f.write(coderevis.text)
            res = subprocess.run(['python','script.py'], capture_output = True, text = True)
            coderevis = client.models.generate_content(model = "gemini-2.0-flash",
                                         contents = ("The function the code to write should be:",query, "The output of the code written for this function was",res.stdout,"Is this acceptable? If acceptable, type yes and nothing else. If unnaceptable, type revised code."), 
                                         config = types.GenerateContentConfig(temperature = 0))
            print(coderevis.text)
    
    
