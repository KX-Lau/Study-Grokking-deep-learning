weight = [0.1, 0.2, 0]


def neural_network(idata, weight):
    prediction = w_sum(idata, weight)
    return prediction


def w_sum(a, b):
    """实现两个向量的加权和, 也成为点积"""

    # 断言, 后面的条件为真继续运行, 为假报错AssertionError
    assert len(a) == len(b)
    output = 0
    for i in range(len(a)):  # 逐元素
        output += a[i] * b[i]
    return output


toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

for i in range(len(toes)):
    idata = [toes[i], wlrec[i], nfans[i]]
    pred = neural_network(idata, weight)
    print(pred)



# 练习向量的操作
def elementwise_multiplication(vec_a, vec_b):
    """逐元素相乘"""
    assert len(vec_a) == len(vec_b)
    vec_res = []
    for i in range(len(vec_b)):
        vec_res.append(vec_a[i] * vec_b[i])
    return vec_res


def elementwise_addition(vec_a, vec_b):
    """逐元素相加"""
    assert len(vec_a) == len(vec_b)
    vec_res = []
    for i in range(len(vec_b)):
        vec_res.append(vec_a[i] + vec_b[i])
    return vec_res


def vector_sum(vec_a):
    vec_sum = 0
    for i in range(len(vec_a)):
        vec_sum += vec_a[i]
    return vec_sum


def vector_average(vec_a):
    vec_avg = 0
    vec_sum = vector_sum(vec_a)
    vec_avg = vec_sum / len(vec_a)
    return vec_avg


print(elementwise_multiplication([1, 2], [3, 4]))
print(elementwise_addition([1, 2], [3, 4]))
print(vector_sum([1, 2, 3, 4]))
print(vector_average([1, 2, 3, 4]))

