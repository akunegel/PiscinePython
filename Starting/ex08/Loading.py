import sys

def ft_tqdm(iterable):
    total = len(iterable)
    for i, item in enumerate(iterable, start=1):
        yield item
        percent = int(100 * i / total)
        bar = bytes((219,)).decode('cp437') * (118 // 2) + '-' * (59 - 118 // 2)
        sys.stdout.write(f"\r{percent}%|{bar}| {i}/{total}")
        sys.stdout.flush()