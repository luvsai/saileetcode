// Last updated: 18/12/2025, 20:21:33
func maxArea(height []int) int {
    hl := len(height)
    i := 0
    j := hl-1
    max_area := 0
    for i<j && i<hl && j > -1 {
        width := j-i
        curr_area :=0
        if height[i] > height[j]{
            curr_area = height[j] * width
            j = j - 1
        } else {
            curr_area = height[i] * width
            i = i  + 1
        }
        if curr_area > max_area {
            max_area = curr_area
        }

    }
    return max_area



    // max_area := 0
    // // h÷l2 := int(hl /2)
    // for i < hl - 1{
    //     j = i + 1
    //     for j< hl{
    //         smallheight := height[i]
    //         smallheight := math.Min(height[i] , height[j])
    //         if height[i] > height[j] {
    //             smallheight = height[j]
    //         }
    //         curr_area := smallheight * (j- i) 

    //         if curr_area > max_area {
    //             max_area = curr_area
    //         }
    //         j +=1
    //     }

    //     i+=1

    // }
    // return max_area
    
}