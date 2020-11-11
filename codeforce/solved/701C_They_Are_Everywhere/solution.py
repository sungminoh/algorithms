def find(pokemons):
    ret = len(pokemons)
    number_of_types = len(set(pokemons))
    how_many_in_range = dict()
    l = 0
    for i in xrange(len(pokemons)):
        pokemon = pokemons[i]
        how_many_in_range[pokemon] = how_many_in_range.get(pokemon, 0) + 1
        while l < i and how_many_in_range.get(pokemons[l], 0) > 1:
            how_many_in_range[pokemons[l]] -= 1
            l += 1
        if len(how_many_in_range) == number_of_types:
            ret = min(ret, i - l + 1)
    return ret


def main():
    _ = int(raw_input())
    pokemons = list(raw_input())
    print find(pokemons)


if __name__ == '__main__':
    main()
