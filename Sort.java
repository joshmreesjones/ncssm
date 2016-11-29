import java.util.Random;
import java.util.Arrays;


/* This is a static sorting class used for sorting Java arrays.
 * Currently, Mergesort and Bubblesort are implemented.
 * 
 * Mergesort is O(nlogn) on average.
 * Bubblesort is O(n^2) on average.
 * 
 * 
 * @author Mitch and Josh Rees-Jones
 */

public class Sort {
	
	/* Sorts Java array using the Mergesort algorithm.
	 * @param array the array to be sorted
	 * @returns sorted array
	 */
	public static int[] mergeSort(int[] array) {
		
		// array of length 1 or 0 is already sorted, also this is the base case
		if(array.length <= 1) {
			return array;
		}

		// Make sublists of left and right half of array
		int[] left = Arrays.copyOfRange(array, 0, array.length/2);
		int[] right = Arrays.copyOfRange(array, array.length/2, array.length);

		// Sort left and right half of array
		left = mergeSort(left);
		right = mergeSort(right);

		// Return left and right halves, now sorted, merged together
		return merge(left, right);
	}
	
	/* Private method to be used only by mergeSort()
	 * @param left left array to be merged
	 * @param right right array to be merged
	 * @returns the two arrays merged together
	 */
	private static int[] merge(int[] left, int[] right) {
		
		// length is used to calculate the size of out so numbers can be added to the end.
		// used like this: out[length - left.length - right.length]
		int length = left.length + right.length;

		// array to be returned. Size is sum of left and right array sizes.
		int[] out = new int[left.length + right.length];
		while(left.length > 0 || right.length > 0) {  // e.g. is there still stuff in the left or right arrays to be merged
			
			// If both left and right arrays have stuff in them
			if(left.length > 0 && right.length > 0) {
				
				// In this block, put the smaller of the left[0] and right[0] in out
				// and remove the element from either left or right.
				if(left[0] >= right[0]) {
					out[length - left.length - right.length] = right[0];
					right = Arrays.copyOfRange(right, 1, right.length);
				}
				else {
					out[length - left.length - right.length] = left[0];
					left = Arrays.copyOfRange(left, 1, left.length);
				}
			}
			// At this point, there is an implication that only left or right has stuff remaining.
			// Not both, not neither. Bam.
			else if(left.length > 0) {
				
				// Add another element in left to out. Once this code block
				// is reached, it will continue adding elements from left until
				// empty. Same with the right array (next code block)
				out[length  - left.length - right.length] = left[0];
				left = Arrays.copyOfRange(left, 1, left.length);
			}

			else if(right.length > 0) {
				out[length - left.length - right.length] = right[0];
				right = Arrays.copyOfRange(right, 1, right.length);
			}

		}

		// We're sorted!
		return out;
	}

	/* Sorts Java array using the Bubble sort algorithm
	 * @parrams array the array to be sorted
	 * @returns the sorted array
	 */
	public static int[] bubbleSort(int[] array) {
		// Sorted set to false whenever two elements are swapped
		// If no elements are swapped, sorted remains true and it
		// it is implied that the array is sorted.
		boolean sorted = false;

		// Placeholder variable for swapping
		int temp;

		while(!sorted) {
			sorted = true;
			for(int i = 0; i < array.length-1; i++) {
				if(array[i] > array[i+1]) { // If true, swap the two elements at i and i+1
					temp = array[i];
					array[i] = array[i+1];
					array[i+1] = temp;

					// Causes for loop to execute again
					sorted = false;
				}
			}
		}

		// We're sorted!
		return array;
	}


	/* Generates integer array of random integers with repeats
	 * @param size the desired size of the array
	 * @returns integer array of random integers
	 */
	public static int[] randomArray(int size) {
		
		// The array to be sorted
		int[] array = new int[size];
		Random rand = new Random();
		for(int i = 0; i < array.length; i++) {
			// Puts random integer from 0 to size at each index of array
			array[i] = rand.nextInt(array.length);
		}
		return array;
	}
	
	/* Test code. Generates two arrays and sorts with Mergesort and Bubblesort.
	 * 
	 */
	public static void main(String[] args) {
		// Random array of size 50
		int[] array = randomArray(50);
		
		// Merge sort
		System.out.println("MergeSort:");
		for(int i = 0; i < array.length; i++) {
			System.out.print(array[i] + ", ");
		}
		System.out.println();
		
		// Sort array, then print
		array = mergeSort(array);
		System.out.println();
		System.out.println("Sorted:");
		for(int i = 0; i < array.length; i++) {
			System.out.print(array[i] + ", ");
		}
		System.out.println();
		System.out.println();


		// Bubble sort
		array = randomArray(40);
		System.out.println("BubbleSort:");
		for(int i = 0; i < array.length; i++) {
			System.out.print(array[i] + ", ");
		}
		System.out.println();
		
		// Sort array, then print
		array = bubbleSort(array);
		System.out.println();
		System.out.println("Sorted:");
		for(int i = 0; i < array.length; i++) {
			System.out.print(array[i] + ", ");
		}
		System.out.println();
	}

}
