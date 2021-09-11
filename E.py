prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input())
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# Ввод, если два числа и более в одну строку
(a, b) = [int(s) for s in input().split()]
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)