import string
import torch
import random

# create a list with all ascii letters
all_letters = "abcdefghrknpABCDEFGHRKNP12345678"
n_letters = len(all_letters)

# maps every ascii character to an individual number
def letterToIndex(letter):
    return all_letters.find(letter)

# creates a tensor resembeling a curtain character
def letterToTensor(letter):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letterToIndex(letter)] = 1
    return tensor

# creates a tensor resembeling a curtain word
def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)] = 1
    return tensor

# converts a tensor to text
def tensorToLine(tensor):
    tensor = tensor.numpy()
    line = ""
    for sub in tensor:
        for li, n in enumerate(sub):
            if n:
                line += all_letters[li]
                
    return line
            
# selects a random element from a list
def randomChoice(l):
    return l[random.randint(0, len(l) - 1)]

def readFile(filepath):
    return open(filepath, encoding='utf-8').read().strip().upper().split('\n')