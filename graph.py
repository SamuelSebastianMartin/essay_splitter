#! /usr/bin/env python3

from matplotlib import pyplot as plt

with open('essay_long.txt', 'r') as f:
    text = f.read()

#  Break the essay into non-empty paragraphs
all_paras = text.split('\n')
paras = [para for para in all_paras if len(para) != 0]  # no empty paras

#  Set up the 'punctuation' characters to check for.
punc = ['.', ',', ';', ':', '?', '(', ')', '@', '/']
#        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#  Set up the frequency distributions to be plotted.
punc_ratios = []
len_paras = []
uppers = []
num_ratios = []

#  Calculate the distributions
for para in paras:
    punc_count = 0
    upper_count = 0
    num_count = 0
    for letter in para:
        #  Count punctuation in para
        if letter in punc:
            punc_count += 1
        #  Count punctuation in para
        elif letter.isupper():
            upper_count += 1
        elif letter.isdigit():
            num_count += 1

    punc_ratio = punc_count/len(para)
    punc_ratios.append(punc_ratio)
    upper_ratio = upper_count/len(para)
    uppers.append(upper_count)
    num_ratio = num_count/len(para)
    num_ratios.append(num_ratio)
    len_paras.append(len(para))

#  Normalise the data for scaling on the graph.
index = [i for i in range(len(punc_ratios))]  # Ordinal number of the para.
norm_len_paras = [l/max(len_paras) for l in len_paras]
norm_uppers = [u/max(uppers) for u in uppers]
norm_punc_ratios = [p * 4 for p in punc_ratios]
norm_nums = [n/max(num_ratios) for n in num_ratios]

#  Print distributions
plt.title('ratio of punctuation per paragraph')
plt.plot(index, norm_uppers, color='orange', label='capitals')
plt.plot(index, norm_nums, color='b', label='numbers')
plt.plot(index, norm_punc_ratios, color='r', label='punct')
plt.bar(index, norm_len_paras, color='y', label='para length')
plt.legend()
plt.show()
