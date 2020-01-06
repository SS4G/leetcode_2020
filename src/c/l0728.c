/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#define TRUE 1
#define FALSE 0
bool isSelfDiv(int x) {
    int tmp = x;
    while (tmp > 0) {
        int digit = tmp % 10;
        if (digit == 0)
            return FALSE;
        if (x % digit != 0) 
            return FALSE;
        tmp /= 10;
    }
    return TRUE;
}

int* selfDividingNumbers(int left, int right, int* returnSize){
    int* result = (int*)malloc(sizeof(int) * 10001);
    int cnt = 0;
    for (int i = left; i <= right; i++) {
        if (isSelfDiv(i)) 
            result[cnt++] = i;
    }
    *returnSize = cnt;
    return result;
}