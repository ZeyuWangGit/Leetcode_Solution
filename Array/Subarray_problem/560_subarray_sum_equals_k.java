public class Solution {
    public int subarraySum(int[] nums, int k) {
        int curr_sum = 0;
        Map<Integer, Integer> map = new HashMap();
        int result = 0;
        map.put(0,1);
        for(int i=0;i<nums.length;i++){
            curr_sum = curr_sum + nums[i];
            if(map.containsKey(curr_sum-k)){
                result=result+map.get(curr_sum-k);
            }
            if(map.containsKey(curr_sum)){
                map.put(curr_sum,map.get(curr_sum)+1);
            }else{
                map.put(curr_sum,1);    
            }
            
        }
        return result;
        
    }
}
