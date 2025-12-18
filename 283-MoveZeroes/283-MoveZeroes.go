// Last updated: 18/12/2025, 20:19:02
func moveZeroes(nums []int)  {
    // action plan: count the number of zeros to append in the end and change and keep a pointer starting from 0 
    // when you encounter element other than zero add this to the pointer position
    arrlen := len(nums)
    i := 0
    j := 0
    for j < arrlen{
        if nums[j] !=0 {
             nums[i] = nums[j]
            i +=1
        }
        j+=1
    }
    for i < arrlen{
        nums[i] = 0
        i+=1
    }
    
}