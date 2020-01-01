LIMIT = int(1e6);
chain_length = LIMIT*[None];

for i in range(LIMIT):
    steps = 1
    cursor = i
    while cursor > 1:
        if cursor < len(chain_length) and chain_length[cursor] is not None:
            chain_length[i] = steps + chain_length[cursor] - 1
            break
        elif cursor % 2 == 0:
            cursor //= 2
            steps += 1
        else:
            cursor = 3*cursor + 1
            steps += 1
    if cursor == 1 or cursor == 0:
        chain_length[i] = steps

print(f'{max(chain_length)} for {chain_length.index(max(chain_length))}')