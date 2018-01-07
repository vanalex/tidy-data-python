import numpy as np
from math import floor, ceil
from matplotlib import pyplot as plt
from scipy.stats import pearsonr

# reading in all data into a NumPy array
all_data = np.loadtxt(open("./data/wine.data", "r"), delimiter=",", skiprows=0, dtype=np.float64)

# load class labels from column 1
y_wine = all_data[:, 0]

# load the class labels
print('Y_WINE ==> ', y_wine)

# conversion of the class labels to integer-type array
y_wine = y_wine.astype(np.int64, copy=False)

# load the 14 features
X_wine = all_data[:, 1:]

print('X_WINE ==> ', X_wine)

# printing some general information about the data
print('\ntotal number of samples (rows):', X_wine.shape[0])
print('total number of features (columns):', X_wine.shape[1])

# printing the 1st wine sample
float_formatter = lambda x: '{:.2f}'.format(x)
np.set_printoptions(formatter={'float_kind':float_formatter})
print('\n1st sample (i.e., 1st row):\nClass label: {:d}\n{:}\n'.format(int(y_wine[0]), X_wine[0]))

print('Class label frequencies')
print('Class 1 samples: {:.2%}'.format(list(y_wine).count(1)/y_wine.shape[0]))
print('Class 1 samples: {:.2%}'.format(list(y_wine).count(2)/y_wine.shape[0]))
print('Class 1 samples: {:.2%}'.format(list(y_wine).count(3)/y_wine.shape[0]))

plt.figure(figsize=(10,8))

bins = np.arange(floor(min(X_wine[:,0])), ceil(max(X_wine[:,0])), 0.15)
print(bins)

max_bin = max(np.histogram(X_wine[:,0], bins=bins)[0])

colors = ('blue', 'red', 'green')

for label,color in zip(
        range(1, 4), colors):

    mean = np.mean(X_wine[:,0][y_wine == label]) # class sample mean
    stdev = np.std(X_wine[:,0][y_wine == label]) # class standard deviation
    plt.hist(X_wine[:,0][y_wine == label],
             bins=bins,
             alpha=0.3, # opacity level
             label='class {} ($$\mu={:.2f}$$, $$\sigma={:.2f}$$)'.format(label, mean, stdev),
             color=color)

plt.ylim([0, max_bin*1.3])
plt.title('Wine data set - Distribution of alocohol contents')
plt.xlabel('alcohol by volume', fontsize=14)
plt.ylabel('count', fontsize=14)
#plt.legend(loc='upper right')

plt.show()

#############################

plt.figure(figsize=(10, 8))

for label, marker, color in zip(
        range(1, 4), ('x', 'o', '^'), ('blue', 'red', 'green')):

    # Calculate Pearson correlation coefficient
    R = pearsonr(X_wine[:, 0][y_wine == label], X_wine[:,1][y_wine == label])
    plt.scatter(x=X_wine[:, 0][y_wine == label], # x-axis: feat. from col. 1
                y=X_wine[:, 1][y_wine == label], # y-axis: feat. from col. 2
                marker=marker, # data point symbol for the scatter plot
                color=color,
                alpha=0.7,
                label='class {:}, R={:.2f}'.format(label, R[0]) # label for the legend
                )

plt.title('Wine Dataset')
plt.xlabel('alcohol by volume in percent')
plt.ylabel('malic acid in g/l')
plt.legend(loc='upper right')

plt.show()

#############################

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

for label,marker,color in zip(range(1,4),('x', 'o', '^'),('blue','red','green')):

    ax.scatter(X_wine[:,0][y_wine == label],
               X_wine[:,1][y_wine == label],
               X_wine[:,2][y_wine == label],
               marker=marker,
               color=color,
               s=40,
               alpha=0.7,
               label='class {}'.format(label))

ax.set_xlabel('alcohol by volume in percent')
ax.set_ylabel('malic acid in g/l')
ax.set_zlabel('ash content in g/l')

plt.title('Wine dataset')

plt.show()

from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

X_train, X_test, y_train, y_test = train_test_split(X_wine, y_wine, test_size=0.30, random_state=123)

print('Class label frequencies')

print('\nTraining Dataset:')
for l in range(1,4):
    print('Class {:} samples: {:.2%}'.format(l, list(y_train).count(l)/y_train.shape[0]))

print('\nTest Dataset:')
for l in range(1,4):
    print('Class {:} samples: {:.2%}'.format(l, list(y_test).count(l)/y_test.shape[0]))




