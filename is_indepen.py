# 조건부 확률을 이용한 종속, 독립 판단하기
'''
독립확률의 조건
flag_1 : A,B 교집합 확률 == A확률*B확률
flag_2 : A확률 == B였을때 A일 확률 or B확률 == A였을때 B일 확률
flag_3 : B였을때 A일 확률 == B가 아니었을때 A일 확률 or A였을때 B일 확률 == A가 아니었을때 B일 확률
'''
def is_indepen(p_a, p_b, p_a_inter_b, p_b_inter_a, p_a_inter_bc, p_ac_inter_b):
    flag_1 = (p_a*p_b == p_a_inter_b)
    p_a_condi_b = p_a_inter_b/p_b
    p_b_condi_a = p_b_inter_a/p_a
    flag_2= (p_a_condi_b==p_a or p_b_condi_a==p_b)
    p_a_condi_bc = p_a_inter_bc/(1-p_b)
    p_b_condi_ac = p_ac_inter_b/(1-p_a)
    flag_3 = (p_a_condi_b==p_a_condi_bc or p_b_condi_a==p_b_condi_ac)
    return True==flag_1==flag_2==flag_3

dice = [1,2,3,4,5,6]

# task 1. 주사위를 던져 2의 배수와 3의 배수가 나올 확률은 독립인가?
p_a = len(list(filter(lambda x:x%2==0, dice)))/len(dice)
p_b = len(list(filter(lambda x:x%3==0, dice)))/len(dice)
p_a_inter_b = len(list(filter(lambda x:x%2==0 and x%3==0, dice)))/len(dice)
p_b_inter_a = len(list(filter(lambda x:x%3==0 and x%2==0, dice)))/len(dice)
p_a_inter_bc = len(list(filter(lambda x:x%2==0 and x%3!=0, dice)))/len(dice)
p_ac_inter_b = len(list(filter(lambda x:x%2!=0 and x%3==0, dice)))/len(dice)

print('task 1.',is_indepen(p_a, p_b, p_a_inter_b, p_b_inter_a, p_a_inter_bc, p_ac_inter_b))

# task 2. 주사위를 던져 짝수가 나올 확률과 소수가 나올 확률은 독립인가?
def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴
p_a = len(list(filter(lambda x:x%2==0, dice)))/len(dice)
p_b = len(list(filter(lambda x:is_prime_num(x), dice)))/len(dice)
p_a_inter_b = len(list(filter(lambda x:x%2==0 and is_prime_num(x), dice)))/len(dice)
p_b_inter_a = len(list(filter(lambda x:is_prime_num(x) and x%2==0, dice)))/len(dice)
p_a_inter_bc = len(list(filter(lambda x:x%2==0 and not is_prime_num(x), dice)))/len(dice)
p_ac_inter_b = len(list(filter(lambda x:x%2!=0 and is_prime_num(x), dice)))/len(dice)

print('task 2.',is_indepen(p_a, p_b, p_a_inter_b, p_b_inter_a, p_a_inter_bc, p_ac_inter_b))