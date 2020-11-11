import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

	public static Scanner scanner = new Scanner(System.in);

	public static String getInputs() {
		String input = scanner.next();
		return input;
	}

	public static String answer(String number) {
		int[] headingZeros = new int[10];
		int[] counter = new int[10];
		int[] firstAppear = new int[10];
		int cntZero = 0;
		Set<Integer> appearedNumber = new HashSet<>();
		for (int i = 0; i < number.length(); i++) {
			Integer digit = Character.getNumericValue(number.charAt(i));
			if (digit == 0) {
				cntZero += 1;
			} else {
				appearedNumber.add(digit);
				if (counter[digit] == 0) {
					firstAppear[digit] = i;
					headingZeros[digit] = cntZero;
				}
				counter[digit] += 1;
			}
		}

		int minRemove = number.length() + 1;
		int choosenNumber = -1;
		for (Integer i : appearedNumber) {
			if (i != 3 && counter[i] % 3 != 0) {
				continue;
			}
			int newMinRemove = number.length() - (counter[0] - headingZeros[i]) - counter[i];
			if (newMinRemove < minRemove) {
				minRemove = newMinRemove;
				choosenNumber = i;
			}
		}
		if(choosenNumber < 0){
			if (cntZero > 0) {
				return "0";
			} else {
				return "-1";
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = firstAppear[choosenNumber]; i < number.length(); i++) {
			Integer digit = Character.getNumericValue(number.charAt(i));
			if (digit == choosenNumber || digit == 0) {
				sb.append(digit);
			}
		}
		return sb.toString();
	}

	public static void main(String[] args) {
		String number = getInputs();
		System.out.println(answer(number));
	}
}
