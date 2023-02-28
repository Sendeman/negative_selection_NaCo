import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics


def gen_AUC(r: int, axis=None):
    samples = []
    with open(f'AUC/english_train_english_test_r_{r}', mode='r') as f:
        for line in f:
            samples.append((float(line.rstrip()), int(0)))
    with open(f'AUC/english_train_tatalog_test_r_{r}', mode='r') as f:
        for line in f:
            samples.append((float(line.rstrip()), int(1)))

    print(samples)
    scores = []
    labels = []
    for sample in samples:
        scores.append(sample[0])
        labels.append(sample[1])
    # print(labels)

    fpr, tpr, _ = metrics.roc_curve(labels, scores)
    auc = metrics.auc(fpr, tpr)

    #create ROC curve
    axis.plot(fpr,tpr, color='orange', label='ROC curve')
    axis.plot([0, 1], [0, 1], color='darkblue', linestyle='--', label='Random Classifier')
    axis.set(xlabel='1 − specificity', ylabel='sensitivity', title=f"negsel2.jar ROC curve for r={r} | AUC={round(auc, 2)}")




    # x, y = [], []
    # for cutoff in [x / 1000.0 for x in range(0, 50000, 5)]:
    #     # cutoff = float(cutoff)
    #     tp = len([i[0] for i in samples if float(i[0]) > cutoff and i[1] == 1])
    #     fp = len([i[0] for i in samples if float(i[0]) > cutoff and i[1] == 0])
    #     tn = len([i[0] for i in samples if float(i[0]) < cutoff and i[1] == 0])
    #     fn = len([i[0] for i in samples if float(i[0]) < cutoff and i[1] == 1])

    #     x.append(1-(tn/(tn+fp)))
    #     # x.append(tn/(tn+fp))
    #     y.append(tp/(tp+fn))
    # auc = metrics.auc(x, y)


    # axis.plot(x, y, color='orange', label='ROC')
    # axis.plot([0, 1], [0, 1], color='darkblue', linestyle='--', label='Random Classifier')
    # axis.set(xlabel='1 − specificity', ylabel='sensitivity', title=f"negsel ROC curve for r={r} | AUC={round(auc, 2)}")

fig, axs = plt.subplots(3, 3)
rs = [1,2,3,4,5,6,7,8,9]
pos = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
for i, r in enumerate(rs):
    gen_AUC(r=r, axis=axs[pos[i][0], pos[i][1]])
axs[2,2].legend(loc='lower right')
plt.tight_layout()
plt.show()



# for r in range(1,9):
#     plt.plot([0,1], [0,1])
#     gen_AUC(r=r)
# plt.tight_layout()
# plt.show()