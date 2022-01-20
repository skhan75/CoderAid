import java.util.Arrays;

/**
 * Square root decomposition allows us to answer queries in sqrt(N) time. As the
 * implementation of these structures
 * is usually simpler than a segment tree, they are a useful tool in a
 * programmer's arsenal.
 */
public class SqrtDecomposition {
    private int a[];
    private long blockSums[];
    private int blockSize;

    public SqrtDecomposition(int input[]) {
        build(input);
    }

    private void build(int[] input) {
        this.blockSize = (int) Math.ceil(Math.sqrt(input.length));
        a = new int[blockSize * blockSize];
        System.arraycopy(input, 0, a, 0, input.length);
        this.blockSums = new long[blockSize];

        for (int i = 0; i < a.length - 1; i++) {
            blockSums[i / blockSize] += a[i];
        }
    }

    /**
     * @param index The index to be updated
     * @param value The value to set the element at specified index
     */
    public void update(int index, int value) {
        final int blockIndex = index / blockSize;
        blockSums[blockIndex] = blockSums[blockIndex] - a[index] + value; // -oldValue +newValue
        a[index] = value;
    }

    /**
     * @param left  The stating index.
     * @param right The ending index.
     * @return The sum from index left to right
     */
    public long query(final int left, final int right) {
        final int startBlockIndex = left / blockSize;
        final int endBlockIndex = right / blockSize;
        long sum = 0;
        // sum of middle blocks between startBlock and endBlock
        for (int i = startBlockIndex + 1; i < endBlockIndex; i++) 
            sum += blockSums[i];
        final int startIndex = left % blockSize;
        final int endIndex = right % blockSize;
        for (int i = startIndex; i < blockSize; i++) 
            sum += a[startBlockIndex * blockSize + i];
        for (int i = 0; i <= endIndex; i++) 
            sum += a[endBlockIndex * blockSize + i];
        return sum;
    }

    @Override
    public String toString() {
        return "SqrtDecomposition{\n" +
                "a=" + Arrays.toString(a) +
                ",\n blockSums=" + Arrays.toString(blockSums) +
                '}';
    }
}

class Main {
    public static void main(String[] args) {
        final SqrtDecomposition sqrtDecomposition = new SqrtDecomposition(new int[] { 1, 2, 6, 7, 9, 3, 1, 9 });
        System.out.println(sqrtDecomposition);
        System.out.println(sqrtDecomposition.query(2, 6));
        sqrtDecomposition.update(5, 7);
        System.out.println(sqrtDecomposition);
        System.out.println(sqrtDecomposition.query(2, 6));
    }
}
 