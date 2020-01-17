uint32_t reverseBits(uint32_t n) {
    uint32_t result = 0;
    for (uint32_t i = 0; i < 32; i++) {
        if ((n & (1u << i)) != 0) {
            //printf("sks %d\n", i);
            result += (1u << (31 - i));
        }
    }
    return result;
}