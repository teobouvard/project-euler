import glob
import os
from collections import defaultdict

import seaborn as sns

extension_names = {
    '.rb':'Ruby',
    '.py':'Python',
    '.c':'C',
    '.cpp':'C++',
    '.java':'Java',
    '.js':'Javascript',
    '.sh':'Bash',
    }

def count_languages(dir):
    counts = defaultdict(int)
    for program in glob.glob(dir):
        ext = os.path.splitext(program)[-1]
        filename = os.path.basename(program)
        if ext in extension_names:
            if not 'X' in filename:
                counts[extension_names[ext]] += 1
        else:
            print(f'{program} has an unkown extension.')
    return counts

if __name__ == '__main__':
    data = count_languages('../problems/*')
    bar_plot = sns.barplot(x = list(data.keys()), y = list(data.values()))
    bar_plot.set(ylabel='Solved problems')
    bar_plot.figure.savefig('barplot.png', dpi=120)
