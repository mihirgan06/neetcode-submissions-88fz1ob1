class Solution {
    //Subset NOT A PERMUTATION
    //so 1,2 not 2,1
    //For each element we have. achoice
    //[1,2,3]
    //first [1] or []
    //From 1 we add 2 or dont add 2
    //Repeat that on right subtree [2] or []
    //Lastly we have option of 3 so 8 Possibilities
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        //res holds all subsets
        List<Integer> subset = new ArrayList<>();
        //subset is your current working path
        dfs(nums, 0, subset, res); //starts recursion at 0
        return res;
        
    }
    private void dfs(int[] nums, int i, List<Integer> subset, List<List<Integer>> res){
        //nums original array

        if (i >= nums.length){
            //i goes through every single element
            res.add(new ArrayList<>(subset));
            return;
        }
        //include in subset
        subset.add(nums[i]);
        dfs(nums, i + 1, subset, res);
        subset.remove(subset.size() - 1); //resets state so next one works at a clean state
        dfs(nums, i + 1, subset, res);


    }
}
