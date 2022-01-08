impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let n = nums.len();
        for j in 1..n{
            for i in 0..j{
                if nums[j] + nums[i] == target{
                    let ai = i as i32;
                    let aj = j as i32;
                    return vec![ai, aj];
                }
            }
        }
        return vec![3, 4];
    }
}