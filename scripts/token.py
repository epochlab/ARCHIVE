#!/usr/bin/env python3

import sys, argparse, random, string

parser = argparse.ArgumentParser()
parser.add_argument('--select', default='alpha', choices=['alpha', 'code'])
parser.add_argument('--len', type=int, default=18)
parser.add_argument('--seg', type=int, default=3)
parser.add_argument('--split', action='store_true', default=True)
parser.add_argument('--data', type=str, default='/usr/share/dict/web2')
parser.add_argument('--count', type=int, default=2)
args = parser.parse_args(sys.argv[1:])

select = args.select
length = args.len
segments = args.seg
dash = length // segments
split = args.split
data = args.data
count = args.count

def alphanumeric(length):
    chars = string.ascii_letters + string.digits
    result = ''.join((random.choice(chars) for i in range(length)))

    if split == True:
        result = '-'.join(result[i:i+dash] for i in range(0, length, dash))

    return result

def code(count):
    word_list = []

    for word in open(data):
        word_list.append(word[:-1].lower())

    val = ''.join(random.choice(word_list) for i in range(count))
    return val.upper()

if select == 'alpha':
    an = alphanumeric(length)
    print("Alpha-numeric string:", an)

if select == 'code':
    code = code(count)
    print("Code:", code)
