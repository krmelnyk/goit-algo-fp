from linked_list import LinkedList, merge_sorted_lists


def main():
    """Run a short demonstration of reverse, sort, and sorted-list merge."""
    linked_list = LinkedList([7, 3, 9, 1, 5])
    print("Original list:")
    linked_list.print_list()

    linked_list.reverse()
    print("Reversed list:")
    linked_list.print_list()

    linked_list.sort()
    print("Sorted list:")
    linked_list.print_list()

    first = LinkedList([1, 4, 8])
    second = LinkedList([2, 3, 7, 10])
    merged = merge_sorted_lists(first, second)
    print("Merged sorted lists:")
    merged.print_list()


if __name__ == "__main__":
    main()
