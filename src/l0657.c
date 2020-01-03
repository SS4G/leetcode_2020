bool judgeCircle(char *moves){
    int x = 0;
    int y = 0;
    for (int i = 0; moves[i] != '\0'; i++) {
        switch (moves[i]) {
            case 'L': x--; break;
            case 'R': x++; break;
            case 'U': y--; break;
            case 'D': y++; break;
        }
    }
    return x == 0 && y == 0;
}