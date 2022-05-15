// https://leetcode.com/problems/next-permutation/


class Solution{


   public void nextPermutation(int[] array) {
        int i = array.length - 2;

        while(i >= 0 && array[i] >= array[i + 1]) i--; 

        if(i >= 0) {    

            int j = array.length - 1;              
            while(array[j] <= array[i]) j--;      
            swap(array, i, j); 

        }

        reverse(array, i + 1, array.length - 1);      
    }

    public void swap(int[] array, int i, int j) {

        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }

    public void reverse(int[] array, int i, int j) {

        while(i < j) swap(array, i++, j--);

    }
}