# valid parenthesis
input1= "()[]{}"
input2="(]"


def isValid(s: str) -> bool:
        open = ['(', '[', '{']
        close = [')', ']','}']
        p = dict(zip(open, close))

        string = []
        for char in s:
            print(char)
            if char in open:
                string.append(char)
            else:
                if len(string) > 0 and char == p[string[-1]]:
                    string.pop()
                else:
                    return False

        return len(string)==0
