public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int cnt = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & (0x01 << i)) != 0)
                cnt++;
        }
        return cnt;
    }
}