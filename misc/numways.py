def numways(exp, result):
    if not exp: return 0
    if len(exp) == 1: return int(eval(exp) == result)
    if len(exp) == 3: return int(eval(exp) == result)
    ways = 0
    zeroways = numways(exp[2:], 0)
    oneways = numways(exp[2:], 1)
    reszero = eval(exp[:2] + "0")
    resone = eval(exp[:2] + "1")
    if reszero == result:
        ways += zeroways
    if resone == result:
        ways += oneways

    res = eval(exp[:3])
    ways += numways(str(res) + exp[3:], result)
    return ways

print numways("0^1", 1)
print numways("1^0^1", 0)
print numways("0&0|1", 1)
