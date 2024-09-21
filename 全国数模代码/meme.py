import random
# def rng(posibility):
#     if random.random() < posibility:
#         return 1
#     else:
#         return 0

# 定义供应商和流程相关的参数
defect_rate_1 = [0.1, 0.2, 0.1, 0.2, 0.1, 0.5]#次品率
purchase_cost_1 = [4, 4, 4, 4, 4, 4]#购买单价
inspection_cost_1 = [2, 2, 2, 1, 8, 2]#检测成本

defect_rate_2 = [0.1, 0.2, 0.1, 0.2, 0.2, 0.05]#次品率
purchase_cost_2 = [18, 18, 18, 18, 18, 18]#购买单价
inspection_cost_2 = [3, 3, 3, 1, 1, 3]#检测成本

assembly_cost = [6, 6, 6, 6, 6, 6]#装配成本
inspection_cost_final = [3, 3, 3, 2, 2, 3]#检测成本
market_price = [56, 56, 56, 56, 56, 56]#市场售价
replacement_loss = [6, 6, 30, 30, 10, 10]#调换损失
disassembly_cost = [5, 5, 5, 5, 5, 40]#拆解费用
length = len(defect_rate_1)
n = 20000

# 定义适应度函数
def eval_solution(individual):
    x1, x2, y, z = individual
    i = 2
    # 固定的最终缺陷率（设为0.1）
    defect_rate_final_effective = [0.1, 0.2, 0.1, 0.2, 0.1, 0.05]
    total_cost = 0
    Num = n * (1 - defect_rate_1[i])* (1 - defect_rate_2[i])

    #零件购买成本
    total_cost += n * purchase_cost_1[i] + n * purchase_cost_2[i]
    # 检验成本
    total_cost += n * x1 * inspection_cost_1[i]  # 是否选择检验供应商1的产品
    total_cost += n * x2 * inspection_cost_2[i]  # 是否选择检验供应商2的产品

    #装配成本
    total_cost += n * assembly_cost[i]
    # 如果进行最终检验，默认所有产品都存在缺陷
    total_cost += n * y * inspection_cost_final[i] 
    total_cost += n * defect_rate_final_effective[i] * y * z * disassembly_cost[i]

    total_cost += n * defect_rate_final_effective[i] * (replacement_loss[i] + purchase_cost_1[i] + purchase_cost_2[i] + assembly_cost[i]) if y != 1 else 0
    total_cost += n * defect_rate_final_effective[i] * z * disassembly_cost[i] if y != 1 else 0
    total_cost += z * (n * defect_rate_final_effective[i] * x1 * purchase_cost_1[i] + 
                                 n * defect_rate_final_effective[i] * x2 * purchase_cost_2[i]) if y != 1 else 0
    return total_cost

Num = 0
while Num <= 10000:
    l = []
    count = []
    x1 = random.randint(0, 1)
    x2 = random.randint(0, 1)
    y = random.randint(0, 1)
    z = random.randint(0, 1)
    individual = [x1, x2, y, z]
    count.append(individual)
    sum = eval_solution(individual)
    l.append(sum)
    Num += 1
id = l.index(min(l))
print(count[id])
print(min(l)/20000)

