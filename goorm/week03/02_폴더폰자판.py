keyboard = {
	"1": [".", ",", "?", "!"],
	"2": ["A", "B", "C"],
	"3": ["D", "E", "F"],
	"4": ["G", "H", "I"],
	"5": ["J", "K", "L"],
	"6": ["M", "N", "O"],
	"7": ["P", "Q", "R", "S"],
	"8": ["T", "U", "V"],
	"9": ["W", "X", "Y", "Z"]
}

result = ""
n = int(input())
string = input()

cur = ""
cnt = -1
for s in string:
	if s != cur:
		if cur:
			l = len(keyboard[cur]) + 1
			r = cnt % l
			result += cur if r == 0 else keyboard[cur][r-1]
		cur = s
		cnt = 0
	else:
		cnt += 1

if cnt != -1:
	l = len(keyboard[cur]) + 1
	r = cnt % l
	result += cur if r == 0 else keyboard[cur][r-1]

print(result)