class Solution {
    private int reverse(int x) {
        return x == 0 ? 1 : 0;
    }

    public int[][] flipAndInvertImage(int[][] A) {
        for (int i = 0; i < A.length; i++) {
            int aiLength = A[i].length % 2 == 0 ? A[i].length / 2: A[i].length / 2 + 1;
            for (int j = 0; j < aiLength; j++) {
                int length = A[i].length;
                int tmpval1 = A[i][j];
                int tmpval2 = A[i][length - 1 - j];
                A[i][j] = reverse(tmpval2);
                A[i][length - 1 - j] = reverse(tmpval1);
            }
        }
        return A;
    }
}