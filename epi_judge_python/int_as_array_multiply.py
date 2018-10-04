from test_framework import generic_test

#Two arrays with integer,multiply

def multiply(num1, num2):

    def multiplyOneDigit(result, digit, num, zeros):
        n = len(num)
        carry = 0
        rIndex = len(result) - 1 - zeros
        #print (num, digit, result)
        for i in range(n-1, -1, -1):
            m = num[i]*digit + carry + result[rIndex]
            result[rIndex] = m%10
            carry = m//10
            rIndex -= 1

        #print ("Carry ", carry)
        while carry:
            result[rIndex] = result[rIndex] + carry
            result[rIndex] = result[rIndex] % 10
            carry = result[rIndex]//10
            rIndex -= 1

    # TODO - you fill in here.
    sign = 1
    if (num1[0] < 0) ^ (num2[0] < 0):
        sign = -1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0 for i in range(len(num1) + len(num2))]
    offset = 0
    for i in range(len(num1)-1, -1, -1):
        multiplyOneDigit(result, num1[i], num2, offset)
        offset += 1

    result1 = []
    i = 0;
    while result[i] == 0:
        i += 1
    for j in range(i, len(result)):
        result1.append(result[j])

    if sign == -1:
        result1[0] = -result1[0]

    return result1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
