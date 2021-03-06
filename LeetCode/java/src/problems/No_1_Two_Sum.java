package problems;

import java.util.Arrays;
import java.util.HashMap;

/*
 * https://oj.leetcode.com/problems/two-sum/
 * Input: numbers={2, 7, 11, 15}, target=9
 * Output: index1=1, index2=2
*/
public class No_1_Two_Sum {

	public static void main(String[] args) {
		No_1_Two_Sum no1 = new No_1_Two_Sum();
		int[] numbers = {3, 2, 4};
		int target = 6;
		System.out.println(Arrays.toString(no1.twoSum(numbers, target)));
	}
	
	public int[] twoSum(int[] numbers, int target) {
		if(numbers.length>=2){
			// use numHM for num2
			HashMap<Integer,Integer> numHM = new HashMap<Integer,Integer>();
			for(int idx1=0; idx1<numbers.length; idx1++){
				int num2 = target - numbers[idx1];
				if (!numHM.isEmpty()&& numHM.containsKey(num2)){
					int[] result = {numHM.get(num2)+1, idx1 +1};
					return result;
				} else {
					numHM.put(numbers[idx1], idx1);
				}
			}
		}
		int[] result = {-1, -1};
		return result;
    }
	
	/**
	 * VersionOne
	 * Exceed Time Limit
	 */
	public int[] VersionOne(int[] numbers, int target) {
		int sum = 0;
		int[] result = {0,0};
		for(int i=0; i<numbers.length-1; i++){
			for(int j=i+1; j<numbers.length; j++){	// use two loops
				sum = numbers[i] + numbers[j];
				 if (sum == target) {
					 result[0] = i;
					 result[1] = j;
					 return result;
				 }
			}
		}
		return result;
	}
	
	/**
	 * VersionTwo
	 * Exceed Time Limit
	 */
	public int[] VersionTwo(int[] numbers, int target) {
		int[] result = {-1, -1};
		if(numbers.length>=2){
			// use numHM for num2
			HashMap<Integer,Integer> numHM = new HashMap<Integer,Integer>();
			for(int idx1=0; idx1<numbers.length; idx1++){
				int num2 = target - numbers[idx1];
				if (!numHM.isEmpty()&& numHM.containsKey(num2)){
					result[0] = numHM.get(num2)+1;	// time consuming
					result[1] = idx1 +1;	// time consuming
					return result;
				} else {
					numHM.put(numbers[idx1], idx1);
				}
			}
		}
		return result;
	}

}