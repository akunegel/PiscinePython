import sys
import shutil


def ft_tqdm(iterable):
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(iterable)
    term_width = shutil.get_terminal_size((80, 20)).columns - 24
    for i, item in enumerate(iterable, start=1):
        yield item

        percent = int(100 * i / total)
        progress_text = f"{percent:3}%|"
        count_text = f"| {i}/{total}"
        fixed_len = len(progress_text) + len(count_text)

        bar_width = max(10, term_width - fixed_len - 2)
        filled = int(bar_width * i / total)
        empty = bar_width - filled
        bar = '█' * filled + '-' * empty

        sys.stdout.write(f"\r{progress_text}{bar}{count_text}")
        sys.stdout.flush()
