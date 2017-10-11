import csv
import numpy as np
import matplotlib.pyplot as plt
import random

def selectCentroids():
    return np.array([(random.uniform(15, 140), random.uniform(0, 100)) for i in range(5)])
def new_center(mu, cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    #for k in keys:
    #    newmu.append(np.mean(cluster[k],axis = 0))
    return newmu

def matched(newmu, oldmu):
    return (set([tuple(a)for a in newmu]) == set([tuple(a)for a in oldmu]))

def cluster_content(X, centroids):
    cluster = {}
    for x in X:
        value = min([(i[0],np.linalg.norm(x - centroids[i[0]]))for i in enumerate(centroids)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster

def plot_cluster(mu,cluster):
    color = 10 * ['r.','g.','k.','c.','b.']
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)

    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()




x = []
with open('Customers.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        x.append([int(row[3]),int(row[4])])

X = np.array(x)
print(X)

plt.scatter(X[:, 0], X[:, 1])
plt.show()
oldcentroids = selectCentroids()
newcentroids = selectCentroids()
cluster = cluster_content(X, oldcentroids)
plot_cluster(oldcentroids,cluster)
while not matched(newcentroids, oldcentroids):
    oldcentroids = newcentroids
    cluster = cluster_content(X, oldcentroids)
    plot_cluster(oldcentroids, cluster)
    newcentroids =new_center(oldcentroids,cluster)