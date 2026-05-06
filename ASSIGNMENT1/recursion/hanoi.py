def hanoi(n, src, aux, dest, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {src} to {dest}")
        return

    hanoi(n-1, src, dest, aux, moves)
    moves.append(f"Move disk {n} from {src} to {dest}")
    hanoi(n-1, aux, src, dest, moves)