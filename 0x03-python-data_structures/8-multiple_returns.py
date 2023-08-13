#!/usr/bin/python3
def multiple_returns(sentence):
    s_len = len(sentence)
    t = (s_len, sentence[0] if s_len > 0 else "None")
    return (t)
