import hashlib
import collections
import re

fiver = re.compile(r'(.)\1\1\1\1')
three = re.compile(r'(.)\1\1')

def md5_hash(salt, index):
    data = (salt + str(index)).encode()
    return hashlib.md5(data).hexdigest()


def stretched_md5_hash(salt, index):
    data = (salt + str(index))
    for _ in range(2017):
        data = hashlib.md5(data.encode()).hexdigest()
    return data


def search_key(salt, h):
    key_cnt = 0

    look_ahead = 1000
    history = collections.deque(maxlen=look_ahead+1)

    pre_index = 0
    while True:
        index = pre_index - look_ahead - 1
        if index >= 0:
            current_hash = history[0][1]
            match = three.search(current_hash)
            if match:
                digit = match[1]
                for i in range(look_ahead):
                    if digit in history[i+1][0]:
                        key_cnt += 1
                        if key_cnt == 64:
                            return index

        pre_hash = h(salt, pre_index)
        found = set(fiver.findall(pre_hash))
        history.append( (found, pre_hash) )

        pre_index += 1


def part1(inp):
    salt = inp.strip()
    return search_key(salt, md5_hash)

def part2(inp):
    salt = inp.strip()
    return search_key(salt, stretched_md5_hash)
