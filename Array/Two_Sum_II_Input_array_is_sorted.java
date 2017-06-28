//My own solution

public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i=0;i<numbers.length;i++){
            map.put(numbers[i],i+1);
        }
        int result[] = new int[2];
        for(int i=0;i<numbers.length;i++){
            if(map.containsKey(target-numbers[i])){
                int value1 = i+1;
                int value2 = map.get(target-numbers[i]);
                if(value1>value2){
                    result[0]=value2;
                    result[1]=value1;
                }else{
                    result[1]=value2;
                    result[0]=value1;
                }
                break;
            }
        }
        return result;
    }
}

//Wiser Solution
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length-1;
        while(i < j)
        {
            if(numbers[i] + numbers[j] == target) return new int[]{i+1, j+1};
            else if(numbers[i] + numbers[j] < target) i++;
            else j--;
        }
        return new int[]{-1, -1};
    }
}