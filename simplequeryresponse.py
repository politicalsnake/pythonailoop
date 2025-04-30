from google import genai
import subprocess
from google.genai import types

the = True
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

    print(response.text)
    the = False

