class Solution {
    public int singleNumber(int[] nums) {
        int z = 0;
        for (int a: nums) {
            z ^= a;
        }
        return z;
    }
}