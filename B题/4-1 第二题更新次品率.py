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

scenarios = {
    '情况1': {'零配件1': {'次品率': 0.1, '购买单价': 4, '检测成本': 2},
              '零配件2': {'次品率': 0.1, '购买单价': 18, '检测成本': 3},
              '成品': {'次品率': 0.1, '装配成本': 6, '检测成本': 3}},
    '情况2': {'零配件1': {'次品率': 0.2, '购买单价': 4, '检测成本': 2},
              '零配件2': {'次品率': 0.2, '购买单价': 18, '检测成本': 3},
              '成品': {'次品率': 0.2, '装配成本': 6, '检测成本': 3}},
    '情况3': {'零配件1': {'次品率': 0.1, '购买单价': 4, '检测成本': 2},
              '零配件2': {'次品率': 0.1, '购买单价': 18, '检测成本': 3},
              '成品': {'次品率': 0.1, '装配成本': 6, '检测成本': 3}},
    '情况4': {'零配件1': {'次品率': 0.2, '购买单价': 4, '检测成本': 1},
              '零配件2': {'次品率': 0.2, '购买单价': 18, '检测成本': 1},
              '成品': {'次品率': 0.2, '装配成本': 6, '检测成本': 2}},
    '情况5': {'零配件1': {'次品率': 0.1, '购买单价': 4, '检测成本': 8},
              '零配件2': {'次品率': 0.2, '购买单价': 18, '检测成本': 1},
              '成品': {'次品率': 0.1, '装配成本': 6, '检测成本': 2}},
    '情况6': {'零配件1': {'次品率': 0.05, '购买单价': 4, '检测成本': 2},
              '零配件2': {'次品率': 0.05, '购买单价': 18, '检测成本': 3},
              '成品': {'次品率': 0.05, '装配成本': 6, '检测成本': 3}},
}

sampling_data = {
    '零配件1': {'k': 5, 'n': 50},
    '零配件2': {'k': 10, 'n': 50},
    '成品': {'k': 8, 'n': 50},
}

alpha_prior = 1
beta_prior = 1
updated_results = []

for scenario_name, scenario_data in scenarios.items():
    result = {'情况': scenario_name}

    k1 = sampling_data['零配件1']['k']
    n1 = sampling_data['零配件1']['n']
    alpha_post1, beta_post1 = bayesian_update(k1, n1, alpha_prior, beta_prior)
    updated_theta1 = expected_defective_rate(alpha_post1, beta_post1)
    result['零配件1_更新次品率'] = updated_theta1

    k2 = sampling_data['零配件2']['k']
    n2 = sampling_data['零配件2']['n']
    alpha_post2, beta_post2 = bayesian_update(k2, n2, alpha_prior, beta_prior)
    updated_theta2 = expected_defective_rate(alpha_post2, beta_post2)
    result['零配件2_更新次品率'] = updated_theta2

    k_prod = sampling_data['成品']['k']
    n_prod = sampling_data['成品']['n']
    alpha_post_prod, beta_post_prod = bayesian_update(k_prod, n_prod, alpha_prior, beta_prior)
    updated_theta_prod = expected_defective_rate(alpha_post_prod, beta_post_prod)
    result['成品_更新次品率'] = updated_theta_prod

    updated_results.append(result)

df = pd.DataFrame(updated_results)
print(df)

df.to_excel('问题2零配件和成品更新次品率.xlsx', index=False)

df.plot(x='情况', kind='bar', stacked=False, figsize=(10, 6), title="各情况中零配件和成品的更新次品率")
plt.ylabel('更新次品率')
plt.show()
