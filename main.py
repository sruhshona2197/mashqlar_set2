# 6-mashq
{i for i in range(2, 51) if all(i % j != 0 for j in range(2, int(i**0.5)+1))}


# 7-mashq
words = ["apple", "banana", "orange", "ice", "kiwi"]
{w for w in words if w[0].lower() in "aeiou"}


# 8-mashq
s = "abracadabra"
{ch for ch in s}


# 9-mashq
{i**3 for i in range(1, 31) if i % 2 == 1}


# 10-mashq
word = "python"
{ord(ch) for ch in set(word)}
