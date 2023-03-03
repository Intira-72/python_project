from sklearn import datasets

iris_dataset = datasets.load_iris()

# print(iris_dataset.keys())
# print(iris_dataset.target_names)
[print(i) for i in iris_dataset.data[0:10]]