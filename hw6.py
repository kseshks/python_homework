import re

def read_file(filename="commands.txt"):
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def build_commands(file):
    commands = []

    for cmd in file:
        parts = cmd.split()

        if parts[0] == "filter":
            arg = cmd[len("filter "):]

            if arg.startswith("/") and arg.endswith("/"):
                regexp = arg[1:-1]
                commands.append(make_filter_regexp(regexp))
            else:
                commands.append(make_filter_contains(arg))

        elif parts[0] == "print":
            fields = [int(p[1:]) for p in parts[1:]]   # список номеров слов
            commands.append(make_print(fields))

        elif parts[0] == "add":
            n1 = int(parts[1][1:])
            n2 = int(parts[2][1:])
            commands.append(make_add(n1, n2))

        elif parts[0] == "replace":
            old = parts[1]
            new = parts[2]
            commands.append(make_replace(old, new))

        elif parts[0] == "go":
            return commands

        else:
            raise ValueError("Неизвестная команда: " + cmd)

    return commands


def make_filter_contains(substr):
    return lambda it: (line for line in it if substr in line)


def make_filter_regexp(pattern):
    regex = re.compile(pattern)
    return lambda it: (line for line in it if regex.search(line))


def make_print(fields):
    def processor(it):
        for line in it:
            words = line.split()
            selected = []
            for i in fields:
                if 0 <= i-1 < len(words):
                    selected.append(words[i-1])
            yield ' '.join(selected)
    return processor


def make_add(n1, n2):
    def processor(it):
        for line in it:
            words = line.split()
            if len(words) >= max(n1, n2):
                try:
                    a = int(words[n1-1])
                    b = int(words[n2-1])
                    words[n1-1] = str(a + b)
                except ValueError:
                    pass
            yield ' '.join(words)
    return processor


def make_replace(old, new):
    if old.startswith("$"):
        index = int(old[1:])
        return lambda it: (
            _replace_by_index(line, index, new)
            for line in it
        )
    else:
        return lambda it: (
            line.replace(old, new)
            for line in it
        )


def _replace_by_index(line, index, new_word):
    words = line.split()
    if 1 <= index <= len(words):
        words[index - 1] = new_word
    return " ".join(words)


def execute_commands(commands, datafile="file.txt"):
    it = (line.rstrip("\n") for line in open(datafile, encoding="utf-8"))

    for stage in commands:
        it = stage(it)

    for line in it:
        print(line)


if __name__ == "__main__":
    file = read_file()
    commands = build_commands(file)
    execute_commands(commands)