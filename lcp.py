### longest common prefix

strings = ['flower', 'flow', 'flight']

prefix = ''
for cmbn in zip(*strings):
    if len(set(cmbn))>1:
        break
    prefix += cmbn[0]
