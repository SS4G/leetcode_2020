char** fizzBuzz(int n, int* returnSize){
    char **result = (char**)malloc(sizeof(char*));
    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            result[i - 1] = "FizzBuzz";
        } 
        else if (i % 3 == 0) {
            result[i - 1] = "Fizz";
        }
        else if (i % 5 == 0) {
            result[i - 1] = "Buzz";
        } 
        else {
            char* buf = (char*)malloc(sizeof(char) * 32);
            result[i - 1] = buf;
            itoa(i, buf, 10);
        }
    }
    return result;
}