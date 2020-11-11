import java.util.*;

public class Main {

	public static Scanner scanner  = new Scanner(System.in);

    public static int[] getInputs(int n){
        int[] inputs = new int[n];
        for (int i=0; i<n; i++){
            inputs[i] = scanner.nextInt();
        }
        return inputs;
    }

    public static int[] eliminate(List<Integer> survives, int ai, int leader) {
    	int targetIndex = (leader + ai) % survives.size();
		int targetNumber= survives.get(targetIndex);
		survives.remove(targetIndex);
    	return new int[]{targetIndex, targetNumber};
	}

    public static int[] answer(int n, int k, int[] a) {
    	Integer[] numbers = new Integer[n];
    	for (int i=0; i<n; i++){
    	    numbers[i] = i+1;
        }
        List<Integer> survives = new LinkedList<>(Arrays.asList(numbers));
        int[] eliminateds = new int[k];
        int leader = 0;
        for (int i=0; i<k; i++) {
        	int[] indexAndNumber = eliminate(survives, a[i], leader);
        	int index = indexAndNumber[0];
        	int number = indexAndNumber[1];
        	leader = index == survives.size() ? 0 : index;
        	eliminateds[i] = number;
		}
        return eliminateds;
    }

    public static String convertToString(int[] arr, String separator) {
		StringJoiner sj = new StringJoiner(separator);
    	for (int i : arr) {
    		sj.add(Integer.toString(i));
		}
		return sj.toString();
	}

    public static void main(String[] args) {
        int n = getInputs(1)[0];
		int k = getInputs(1)[0];
		int[] a = getInputs(k);
        int[] eliminates = answer(n, k, a);
		System.out.println(convertToString(eliminates, " "));
	}
}

