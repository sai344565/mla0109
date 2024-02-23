def towers_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        towers_of_hanoi(n-1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        towers_of_hanoi(n-1, auxiliary, target, source)
towers_of_hanoi(3, 'A', 'C', 'B')
