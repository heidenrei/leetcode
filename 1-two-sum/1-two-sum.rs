use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let n = nums.len();
        let mut s = HashMap::new();
        for i in 0..n{
            let ai = i as i32;
            let keyi = target - nums[i];
            
            if s.contains_key(&keyi) {
                match s.get(&keyi) {
                    Some(&aj) => return vec![aj, ai],
                    _ => println!("{}", "")
            }
            }
            
            // if s.contains_key(&keyi) {
            //     let aj = s.get(&keyi) as i32;
            //     return vec![aj, ai];
            // }

            s.insert(nums[i], ai);
        }
        return vec![-1, -1];

    }
}