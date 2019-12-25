import glob
import os
from collections import defaultdict

import seaborn as sns

extension_names = {
    '.rb':'Ruby',
    '.py':'Python',
    }

def count_languages(dir):
    counts = defaultdict(int)
    for program in glob.glob(dir):
        ext = os.path.splitext(program)[-1]
        if ext in extension_names:
            counts[extension_names[ext]] += 1
        else:
            print(f'{program} has an unkown extension.')
    return counts

if __name__ == '__main__':
    data = count_languages('../problems/*')
    bar_plot = sns.barplot(x = list(data.keys()), y = list(data.values()))
    bar_plot.set(ylabel='Solved problems')
    bar_plot.figure.savefig('barplot.png', dpi=120)
