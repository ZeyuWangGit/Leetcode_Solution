public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> result = new ArrayList<Integer>();
        for(int i = 0 ; i < nums.length ; i++ ){
            int val = Math.abs(nums[i]);
            if(nums[val - 1]>0)
                nums[val - 1] = -nums[val - 1];
        }
        for(int i=0;i<nums.length;i++){
            if(nums[i]>0){
                result.add(i+1);
            }
        }
        return result;
    }
}

// Mark index array to slove the problem