# is a string a permutation of another string?
string1 = 'aabcdp'
string2 = 'bdacap'
string3 = 'hello'

def is_permute(string1, string2):
    if len(string1) != len(string2):
        return False

    return sorted(string1) == sorted(string2)

def is_permute2(string1, string2):
    if len(string1) != len(string2):
        return False

    freq_dict = {}
    for char in string1:
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1

    for char in string2:
        if char not in freq_dict:
            return False
        else:
            if string2.count(char) != freq_dict[char]:
                return False

    return True



# string compression
s = 'aabcccca'
def s_compression(s):
    char_list = []
    i = 0
    count = 1
    while i < len(s)-1:
        if s[i]==s[i+1]:
            count += 1
        else:
            char_list.append(s[i])
            char_list.append(count)
            count = 1
        i += 1
    char_list.append(s[i])
    char_list.append(count)

    sc = ''
    for char in char_list:
        sc += str(char)

    return sc


# check if two strings are one edit away
s1 = 'pales, pales'
s2 = 'pale, pale'

def one_away(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 - n2 < -1 or n1 - n2 > 1:
        return False
    n = min(n1, n2) - 1
    i = 0
    count = 0
    while i < n:
        if s1[i] != s2[i]:
            i += 1
            count += 1
        i += 1

    if n1 == n2:
        return count <= 1
    else:
        return count == 0



### word ladder
start ="hit"
end = "cog"
word_dict =["hot","dot","dog","lot","log"]


def word_distance(w1, w2):
    n = len(w1)
    bool_vector = [w1[i]==w2[i] for i in range(n)]
    if sum(bool_vector) == n - 1:
        return True
    else:
        return False

from collections import defaultdict
leaves_dict = defaultdict(set)
all_words = word_dict + [start] + [end]
for word1 in all_words:
    for word2 in all_words:
        if word1 != word2 and word_distance(word1, word2):
            leaves_dict[word1].add(word2)

visited = set()
ladder = [start]
visited.add(start)
level = 0
while ladder:
    level += 1
    for i in range(len(ladder)):
        current_word = ladder.pop(0)
        for word in leaves_dict[current_word]:
            if word == end:
              print(level, visited, ladder)
            else:
              if word not in visited:
                  visited.add(word)
                  ladder.append(word)
