class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        sum_ones = 0
        mask = 1
        bits = int(A).bit_length()
        for i in range(bits):
            sum_ones += A & mask
            A = A>>1
        return sum_ones


sol = Solution()
print(sol.numSetBits(16))