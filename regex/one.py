import re


t = "hello world hello"

p = re.match(r'h.llo',t)

# x = p.finditer(t)
print(p)
# print(x.group())
# print(x.span())
# print(x.start())
# print(x.end())

# -----------EMAIL-REGEX----------
# ^([a-zA-Z0-9\.\-\_]+)@([a-zA-Z]+)\.([a-zA-Z]{2,5})$/gm
# /^([\w\.\-\_]+)@([\w]+)\.([\w]{2,5})$/gm


# -------------HEX COLER------------
# /^#([a-f0-9]{3,6})/gm





