const = "1d47faf54f84dc393a4a015a8f190e36"
key = ""
good_boy = ""
# Correct = 1a4fa@

enc_flag = [
    0x2f, 0x1d, 0x14, 0x14,
    0x58, 0x08, 0x14, 0x19,
    0x01, 0x1d, 0x1c, 0x59,
    0x58, 0x2c, 0x10, 0x11,
    0x0b, 0x58, 0x11, 0x0b,
    0x58, 0x0c, 0x10, 0x1d,
    0x58, 0x17, 0x16, 0x14,
    0x01, 0x58, 0x0e, 0x19,
    0x14, 0x11, 0x1c, 0x58,
    0x1e, 0x14, 0x19, 0x1f
]

key += const[0]
key += const[5]
key += const[8]
key += const[9]
key += key[1]
key += '@'

for c in enc_flag:
    good_boy += chr(c ^ 0x78)

if key == "1a4fa@":
    print "Key: %s" % key
    print good_boy