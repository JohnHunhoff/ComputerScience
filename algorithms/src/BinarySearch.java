public class BinarySearch {
    public static void main(String[] args) {

        int[] orderedList = {87, 21, 45, 93};

        System.out.println(binarySearch(orderedList, 87));
    }

    public static int binarySearch(int[] list, int item) {
        if (listEmpty(list)) { return -1; }

        int lowIndex = 0;
        int highIndex = list.length - 1;

        while (lowIndex <= highIndex) {
            int midIndex = (lowIndex + highIndex) / 2;
            int kick = list[midIndex];

            if (isEquals(kick, item)) {
                return midIndex;
            } else if (isGreaterThan(kick, item)) {
                highIndex = midIndex - 1;
            } else if (isLessThan(kick, item)) {
                lowIndex = midIndex + 1;
            }
        }

        return -1;
    }

    public static boolean listEmpty(int[] list) {
        int sizeOfList = list.length;
        if (sizeOfList == 0) {
            return true;
        }
        return false;
    }

    public static boolean isEquals(int kick, int item) {
        if (kick != item) {
            return false;
        }
        return true;
    }

    public static boolean isGreaterThan(int kick, int item) {
        if ( kick < item) {
            return false;
        }
        return true;
    }

    public static boolean isLessThan(int kick, int item) {
        if (kick > item) {
            return false;
        }
        return true;
    }



}
