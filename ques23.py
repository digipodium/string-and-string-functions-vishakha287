x= input('enter:')
start_idx = 0
while True:
    idx = x.find('fyi',start_idx)
    if idx == -1:
        break
    print(f'`fyi` word found at {idx}')
    start_idx = idx + 1