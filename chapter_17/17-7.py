"""
17.7 Baby Names: Each year, the government releases a list of the 10000 most common baby names
and their frequencies (the number of babies with that name). The only problem with this is that
some names have multiple spellings. For example, "John" and ''.Jon" are essentially the same name
but would be listed separately in the list. Given two lists, one of names/frequencies and the other
of pairs of equivalent names, write an algorithm to print a new list of the true frequency of each
name. Note that if John and Jon are synonyms, and Jon and Johnny are synonyms, then John and
Johnny are synonyms. (It is both transitive and symmetric.) In the final list, any name can be used
as the "real" name.
EXAMPLE
Input:
Names: John (15), Jon (12), Chris (13), Kris (4), Christopher (19)
Synonyms: (Jon, John), (John, Johnny), (Chris, Kris), (Chris, Christopher)
Output: John (27), Kris (36)
Hints:#478, #493, #512, #537, #586, #605, #655, #675, #704
"""


def real_name_freq(freq, syn):
	syn_hash = {}
	for s in syn:
		#print(s)
		#print(syn_hash)
		if s[0] not in syn_hash:
			syn_hash[s[0]] = [s[1]]
		else:
			syn_hash[s[0]].append(s[1])

		if s[1] not in syn_hash:
			syn_hash[s[1]] = [s[0]]
		else:
			syn_hash[s[1]].append(s[0])
	print(syn_hash)
	syn_hash_freq = {}
	for key,value in syn_hash.items():
		names = value
		if names != None:
			for name in names:
				if syn_hash[name]:
					names = names + syn_hash[name]
			for name in names:
				syn_hash[name] = None
		syn_hash_freq[str(names)] = 0

		for key,value in freq.items():
			if names == None:
				continue
			if key in names:
				syn_hash_freq[str(names)] += value

	return syn_hash_freq

names = {"John":15, "jon":12,"Chris":13, "Kris":4, "Christopher":19}
synonyms = [("Jon", "John"), ("John", "Johnny"), ("Chris", "Kris"), ("Chris", "Christopher")]
print(real_name_freq(names, synonyms))
