'''
lite mikhad az noghte a be noghte b bere.
2 no ghatar darim
1. az x mire be x+1
2. az k*x mire be k*(x+1)
har 2 ta ghatar 1min tul mikeshe az ye noghte be noghte badish beran.
'''
k, a, b = map(int, input().split())
if a > b:
    b, a = a, b

quotient_a = a // k
quotient_b = b // k
sub_q = quotient_b - quotient_a
remainder_a = a % k
remainder_b = b % k

answers = [b - a, sub_q + remainder_a + remainder_b, sub_q + k - remainder_a + remainder_b - 1,
           sub_q + remainder_a + k - remainder_b + 1, sub_q + 2 * k - remainder_a - remainder_b]
answers.sort()

print(answers[0])
