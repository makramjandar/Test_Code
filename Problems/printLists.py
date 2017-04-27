#!/Applications/anaconda/envs/Python3/bin


def main():
    # Test suite
    test_list_1 = ["puppy", "kitten", "lion cub"]
    test_list_2 = ["lettuce",
                    "bacon",
                    "turkey",
                    "mayonnaise",
                    "tomato",
                    "white bread"]

    pretty_print_lists(test_list_1)
    pretty_print_lists(test_list_2)


def pretty_print_lists(l):
    output = ""
    last_index = len(l) - 1
    for i, item in enumerate(l):
        if i == last_index:
            output += "and {}".format(item)
        else:
            output += "{}, ".format(item)

    print(output)
    return None


if __name__ == '__main__':
    main()
