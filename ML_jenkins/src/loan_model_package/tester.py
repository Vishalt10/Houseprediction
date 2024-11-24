import data_loader

dataset=data_loader.data_loader()

print(dataset.isnull().sum())

dataset=data_loader.data_imputation(dataset)


print(dataset.isnull().sum())