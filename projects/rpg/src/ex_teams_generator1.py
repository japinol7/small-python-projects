import random
import os


FILE_NAMES = os.path.join('..', 'res', 'names', 'names_anime1.txt')
GROUP_SEPARATOR = f"{'-' * 10}"
N_MEMBERS = 3
N_TEAMS = 42


def calc_team(team_name, names, names_sel, n_members=3):
    if len(names_sel)+n_members > len(names):
        print(f"Error: {team_name}: Not enough Characters "
              f"to generate this team!\n{GROUP_SEPARATOR}")
        return
    print(f"{team_name}\n{GROUP_SEPARATOR}")
    for _ in range(n_members):
        name = None
        while not name:
            name = random.choice(names)
            if name in names_sel:
                name = None
                continue
            names_sel += [name]
            print(name)


def print_names_remaining(names_remaining):
    if len(names_remaining) < N_MEMBERS:
        print(f"Remaining Characters:\n{GROUP_SEPARATOR}")
        for name in names_remaining:
            print(f"{name}")
    else:
        print(f"Remaining Characters: {len(names_remaining)}\n"
              f"{GROUP_SEPARATOR}")


def main():
    names = set()
    names_sel = []

    with open(FILE_NAMES, 'r') as fin:
        for line in fin:
            line_st = line.strip()
            if line_st:
                names.add(line_st)
    names = list(names)

    for i in range(N_TEAMS):
        calc_team(f'Team {i+1}', names, names_sel, N_MEMBERS)
        print()

    names_remaining = list(set(names) - set(names_sel))
    if names_remaining:
        print_names_remaining(names_remaining)


if __name__ == '__main__':
    main()
