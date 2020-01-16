class Solution {
    public boolean hasAlternatingBits(int n) {
        boolean[] bits = new boolean[32];
        int maxBit = 0;
        for (int i = 0; i < 32; i++) {
            if (((0x01 << i) & n) != 0) {
                bits[i] = true;
                maxBit = i;
            } 
            else {
                bits[i] = false;
            }
        }

        for (int i = 0; i < maxBit; i++) {
            if (bits[i] == bits[i + 1]) {
                return false;
            }
        }
        return true;
    }
}