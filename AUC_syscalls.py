import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np
from pathlib import Path
import sys

def unpack_file(res: Path, labels: Path):
    results_list = []
    labels_list = []

    print(res, labels)
    with open(res, "r") as res, open(labels , "r") as labels:
        for i, (line, label) in enumerate(zip(res, labels)):
            line = line.strip("\n")
            line = line.strip(" ")
            preds = line.split(" ")
            
            int_preds = list(map(float, preds))
            avg = sum(int_preds) / len(int_preds)

            results_list.append(avg)
            labels_list.append(np.float64(label.strip("\n")))   
    return results_list, labels_list
  

def gen_AUC(rs: tuple, n: int, axis=None, pref="unm"):
    max_auc=0
    max_r=None
    for r in rs:
        res = f"syscalls/negselresults/{pref}_n_{n}_r_{r}"
        labels = f"syscalls/snd-{pref}/all.labelss"
        results_list, labels_list = unpack_file(res, labels)

        fpr , tpr, _ = metrics.roc_curve(labels_list[:-1], results_list[1:])
        auc = metrics.auc(fpr, tpr)

        #Track maximum AUC and Max r
        if auc>max_auc: 
            max_auc = auc
            max_r=r

        axis.plot(fpr,tpr, label=f'r={r}')
    axis.plot([0, 1], [0, 1], color='darkblue', linestyle='--', label='Random Classifier')
    axis.set(xlabel='1 − specificity', ylabel='sensitivity', title=f"negsel2.jar ROC curve for n={n} | Max_AUC={round(auc, 2)}, with r={max_r}")



fig, axs = plt.subplots(2, 2)
pos = [(0,0), (0,1), (1,0), (1,1)]
ns=[]
rs=[]
for n in range(4,8): #Populate n parameters and r parameters same way as bash script
    ns.append(n)
    rtemp=[]

    r = 1
    while 2 <= n-r:
        rtemp.append(r)

        r+=1
    rs.append(rtemp)

for i, n in enumerate(ns):
    gen_AUC(rs=rs[i], n=n, axis=axs[pos[i][0], pos[i][1]])    

axs[1,1].legend(loc='lower right')
plt.tight_layout()
plt.show()
