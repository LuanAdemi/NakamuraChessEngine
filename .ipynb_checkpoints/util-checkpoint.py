import string
import torch
import random
import numpy as np

def boardToTensor(board, c):
    boardArray = np.array([a.split(" ") for a in str(board).split("\n")])
    
    wPMask = np.array([boardArray == "P"], dtype=np.int)
    bPMask = np.array([boardArray == "p"], dtype=np.int)
    wBMask = np.array([boardArray == "B"], dtype=np.int)
    bBMask = np.array([boardArray == "b"], dtype=np.int)
    wNMask = np.array([boardArray == "N"], dtype=np.int)
    bNMask = np.array([boardArray == "n"], dtype=np.int)
    wRMask = np.array([boardArray == "R"], dtype=np.int)
    bRMask = np.array([boardArray == "r"], dtype=np.int)
    wQMask = np.array([boardArray == "Q"], dtype=np.int)
    bQMask = np.array([boardArray == "q"], dtype=np.int)
    wKMask = np.array([boardArray == "K"], dtype=np.int)
    bKMask = np.array([boardArray == "k"], dtype=np.int)
    tensor = np.zeros((7,8,8))
    
    tensor[0] = wPMask - bPMask
    tensor[1] = wBMask - bBMask
    tensor[2] = wNMask - bNMask
    tensor[3] = wRMask - bRMask
    tensor[4] = wQMask - bQMask
    tensor[5] = wKMask - bKMask
    
    if c=="b":
        tensor[6] = np.full((8,8), 1)
    return torch.FloatTensor(tensor).view(1,7,8,8)

def moveToTensor(move):
    boardLetters = "abcdefgh"
    moveArray = list(str(move))[:4]
    tensor = np.zeros((4,4,4))
    for i, l in enumerate(moveArray):
        tmp = np.zeros((16))
        if i%2 == 0:
            index = boardLetters.find(l)
            tmp[index] = 1
        else:
            index = int(l)-1
            tmp[index] = 1
        tensor[i] = tmp.reshape((4,4))
    return torch.FloatTensor(tensor)

def tensorToMove(tensor):
    boardLetters = "abcdefgh"
    move = ""
    for i, m in enumerate(tensor):
        m.reshape((16))
        if i%2 == 0:
            move += boardLetters[np.argmax(m[:8])]
        else:
            move += str(np.argmax(m[:8]).item() + 1)
    return move