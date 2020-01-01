import glob
import os

def count_remaining(dir):
    done = set()
    for program in glob.glob(dir):
        filename = os.path.basename(program)
        if 'X' not in filename:
            done.add(int(filename[:3]))
    return set(range(1, 500)) - done


if __name__ == '__main__':
    remaining = count_remaining('../problems/*')
    print(f'Remaining problems : {list(remaining)[:10]} ...')
