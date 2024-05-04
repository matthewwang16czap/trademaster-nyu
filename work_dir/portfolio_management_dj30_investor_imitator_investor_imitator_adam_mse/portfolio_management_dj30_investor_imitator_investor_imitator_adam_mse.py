data = dict(
    type='PortfolioManagementDataset',
    data_path='data/portfolio_management/dj30',
    train_path='data/portfolio_management/dj30/train.csv',
    valid_path='data/portfolio_management/dj30/valid.csv',
    test_path='data/portfolio_management/dj30/test.csv',
    tech_indicator_list=[
        'high', 'low', 'open', 'close', 'adjcp', 'zopen', 'zhigh', 'zlow',
        'zadjcp', 'zclose', 'zd_5', 'zd_10', 'zd_15', 'zd_20', 'zd_25', 'zd_30'
    ],
    length_day=10,
    initial_amount=100000,
    transaction_cost_pct=0.0001,
    test_dynamic_path='data/portfolio_management/dj30/test_with_label.csv',
    test_dynamic='-1')
environment = dict(type='PortfolioManagementInvestorImitatorEnvironment')
agent = dict(
    type='PortfolioManagementInvestorImitator',
    memory_capacity=1000,
    gamma=0.99,
    policy_update_frequency=500)
trainer = dict(
    type='PortfolioManagementInvestorImitatorTrainer',
    epochs=10,
    work_dir=
    'work_dir/portfolio_management_dj30_investor_imitator_investor_imitator_adam_mse',
    if_remove=False)
loss = dict(type='MSELoss')
optimizer = dict(type='Adam', lr=0.001)
act = dict(type='MLPCls', input_dim=638, dims=[128], output_dim=5)
task_name = 'portfolio_management'
dataset_name = 'dj30'
net_name = 'investor_imitator'
agent_name = 'investor_imitator'
optimizer_name = 'adam'
loss_name = 'mse'
work_dir = 'work_dir/portfolio_management_dj30_investor_imitator_investor_imitator_adam_mse'
