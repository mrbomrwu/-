import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import beta
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

def bayesian_update(k, n, alpha_prior=1, beta_prior=1):
    alpha_post = alpha_prior + k
    beta_post = beta_prior + (n - k)
    return alpha_post, beta_post

def expected_defective_rate(alpha_post, beta_post):
    return alpha_post / (alpha_post + beta_post)

components = {
    '零配件1': {'次品率': 0.1, '购买单价': 2, '检测成本': 1},
    '零配件2': {'次品率': 0.1, '购买单价': 8, '检测成本': 1},
    '零配件3': {'次品率': 0.1, '购买单价': 12, '检测成本': 2},
    '零配件4': {'次品率': 0.1, '购买单价': 2, '检测成本': 1},
    '零配件5': {'次品率': 0.1, '购买单价': 8, '检测成本': 1},
    '零配件6': {'次品率': 0.1, '购买单价': 12, '检测成本': 2},
    '零配件7': {'次品率': 0.1, '购买单价': 8, '检测成本': 1},
    '零配件8': {'次品率': 0.1, '购买单价': 12, '检测成本': 2},
}

semi_products = {
    '半成品1': {'次品率': 0.1, '装配成本': 8, '检测成本': 4, '拆解费用': 6},
    '半成品2': {'次品率': 0.1, '装配成本': 8, '检测成本': 4, '拆解费用': 6},
    '半成品3': {'次品率': 0.1, '装配成本': 8, '检测成本': 4, '拆解费用': 6},
}

final_product = {
    '成品': {'次品率': 0.1, '装配成本': 8, '检测成本': 6, '拆解费用': 10, '售价': 200, '调换损失': 40}
}

sampling_data = {
    '零配件1': {'k': 5, 'n': 50},
    '零配件2': {'k': 10, 'n': 50},
    '零配件3': {'k': 8, 'n': 50},
    '零配件4': {'k': 3, 'n': 50},
    '零配件5': {'k': 7, 'n': 50},
    '零配件6': {'k': 2, 'n': 50},
    '零配件7': {'k': 6, 'n': 50},
    '零配件8': {'k': 4, 'n': 50},
    '半成品1': {'k': 6, 'n': 50},
    '半成品2': {'k': 9, 'n': 50},
    '半成品3': {'k': 5, 'n': 50},
    '成品': {'k': 7, 'n': 50},
}

alpha_prior = 1
beta_prior = 1
updated_results = []

for item_name, data in {**components, **semi_products, '成品': final_product}.items():
    k = sampling_data[item_name]['k']
    n = sampling_data[item_name]['n']

    alpha_post, beta_post = bayesian_update(k, n, alpha_prior, beta_prior)
    updated_theta = expected_defective_rate(alpha_post, beta_post)

    updated_results.append({
        '项目': item_name,
        '更新次品率': updated_theta
    })

df = pd.DataFrame(updated_results)
print(df)

df.to_excel('问题3零配件半成品成品更新次品率.xlsx', index=False)

df.plot(x='项目', kind='bar', stacked=False, figsize=(10, 6), title="问题3: 零配件、半成品和成品的更新次品率")
plt.ylabel('更新次品率')
plt.show()
