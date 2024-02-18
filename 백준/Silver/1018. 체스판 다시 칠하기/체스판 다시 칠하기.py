row, col = map(int, input().split())

board = []
for i in range(row):
    line = list(input())
    board.append(line)
result = []
def board_print():
    for i in range(row-7):
        for j in range(col-7):
            draw1 = 0
            draw2 = 0
            
            board_ = []
            for r in range(0+i, 8+i):
                line_ = []
                for c in range(0+j, 8+j):
                    if r % 2 == 0:
                        # black 만 확인
                        # white 만 확인
                        if c % 2 == 0:
                            if board[r][c] != 'W':
                                draw1 += 1
                            elif board[r][c] != 'B':
                                draw2 += 1
                        else:
                            if board[r][c] != 'B':
                                draw1 += 1
                            elif board[r][c] != 'W':
                                draw2 += 1
                    else:
                        if c % 2 == 1:
                            if board[r][c] != 'W':
                                draw1 += 1
                            elif board[r][c] != 'B':
                                draw2 += 1
                        else:
                            if board[r][c] != 'B':
                                draw1 += 1
                            elif board[r][c] != 'W':
                                draw2 += 1

                    line_.append(board[r][c])
                board_.append(line_)
            result.append(draw1)
            result.append(draw2)
    print(min(result))
board_print()