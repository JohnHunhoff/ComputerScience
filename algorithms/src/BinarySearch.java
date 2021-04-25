import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BinarySearch {
    public static void main(String[] args) {
        List<Integer> integerArrayList = new ArrayList<>();
        integerArrayList.add(80); // 3
        integerArrayList.add(21); // 2
        integerArrayList.add(8);  // 1
        integerArrayList.add(95); // 4
        integerArrayList.add(1);  // 0
        Collections.sort(integerArrayList);

        System.out.println(binarySearch(integerArrayList, 80));
    }

    public static int binarySearch(List<Integer> list, int number) {
        if (list.isEmpty()) {
            return -1;
        }

        int lowIndex = 0;
        int highIndex = list.size() - 1;

        while (lowIndex <= highIndex) {
            int guess = (lowIndex + highIndex) / 2;
            int kick = list.get(guess);

            if (kick == number) {
                return guess;
            } else if (kick < number) {
                lowIndex = guess;
            } else if (kick > number) {
                highIndex = guess;
            }

        }
        return -1;
    }

    }

