# basic-mod1

## Category

Cryptography

## Tools Used

Python

## Key Takeaways

- Use of the modulo (`%`) operator can save time and effort
- Basic file reading using the `with` keyword is helpful and keeps code clean

## Question

We found this weird message being passed around on the servers, we think we have a working decrpytion scheme.

Download the message [here](./message.txt).

Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.

Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Process

For this problem, the first aspect we need to consider is how to read values from a file. The cleanest way to do this is through the use of the `with` keyword, creating a scope that automatically closes the file when exited:

```py
with open({file}) as f:
    # code goes here
```

From here, we can read all the values from our text file as a single string using the `.read()` function. Looking at our provided file, each of the 
