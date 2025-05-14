This is a school project
It is mostly finished

What its for - 
  Writing Python programs with AI, with an emphasis on the output being high quality through revision

How it works - 
  The code uses the Gemini AI Python API to write and revise Python programs and achieves high-quality output.

What it does - 
  The code will create, then revise a program based on an initial prompt. The program will automatically create the Python program files it writes, and then run them. DON'T TELL IT TO WRITE A PROGRAM YOU DON'T WANT TO RUN... CUZ IT WILL.

Run in a Python3 terminal - you need a Gemini API key, which you can get for free.
Due to the free API only having 15 uses in a given period of time, you can only have 15 revisions.

Example:
Enter gemini API key:
[Put your API key here]
You need at least 3 tokens to work. You start with 15. If you run out, code will stop.
Enter input:
print e - [this is your initial input]
Your input was:  print e  would you like to revise?
no - [you wanna revise?]
Initial program: - [DONT use this program]

def print_e():
  """Prints the letter 'e' using asterisks."""

  e_pattern = [
      "*****",
      "*    ",
      "*****",
      "*    ",
      "*****",
  ]

  for row in e_pattern:
    print(row)

if __name__ == "__main__":
  print_e()


Initial output:
*****
*
*****
*
*****

revision number: 1
tokens used: 2
revised code
```python
def print_pattern():
  """Prints the specified pattern."""
  print("*****")
  print("*")
  print("*****")
  print("*")
  print("*****")

if __name__ == "__main__":
  print_pattern()
```

Revised code or yes, it works: yes - [It works!]

Out: *****
*
*****
*
*****

countfirst - [This is for debugging, ignore it.]

Final output: - [What the final program spits out]
*****
*
*****
*
*****

Final code: - [The program to use]

def print_e():
  """Prints the letter 'e' using asterisks."""

  e_pattern = [
      "*****",
      "*    ",
      "*****",
      "*    ",
      "*****",
  ]

  for row in e_pattern:
    print(row)

if __name__ == "__main__":
  print_e()


Query count: 3
You have enough tokens. Code starting over. - [If you have enough tokens, the code will start over]
Enter input: 
