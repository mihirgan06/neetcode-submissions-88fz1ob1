class Solution {
    /**
    Given an integer array nums and an integer k, return the k most frequent elements within the array
    */
    public int[] topKFrequent(int[] nums, int k) {
        // 1. Build frequency map: num -> count
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // 2. Buckets: index = frequency, value = list of numbers with that frequency
        List<Integer>[] buckets = new ArrayList[nums.length + 1];

        for (int num : map.keySet()) {
            int freq = map.get(num);
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(num);
        }

        // 3. Collect top k from highest frequency down
        List<Integer> result = new ArrayList<>();
        for (int freq = buckets.length - 1; freq >= 0 && result.size() < k; freq--) {
            if (buckets[freq] != null) {
                result.addAll(buckets[freq]);
            }
        }

        // 4. Convert to array of size k
        int[] answer = new int[k];
        for (int i = 0; i < k; i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }
}
