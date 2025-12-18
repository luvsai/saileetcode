// Last updated: 18/12/2025, 20:16:56
func mergeAlternately(word1 string, word2 string) string {
    
    i := 0
    lw1 := len(word1)
    lw2 := len(word2)
    word3 := ""
    temp := lw1
    if (lw1 > lw2) {
        temp= lw2
    }
    for i< temp {
         word3 = word3 + string(word1[i] ) + string(word2[i])
        i += 1
    }
    if (lw1 > lw2){
        word3  = word3 + word1[i:]
    }else{
        word3  = word3 + word2[i:]
    }
    
    return word3

    
    
    // for i<lw1 || i < lw2 {
    //     if i<lw1{
    //      word3 = word3 + string(word1[i] )
    //     }
    //     if  i < lw2 {
    //         word3 = word3 + string(word2[i])
    //     }

    //     i += 1
    // }
    // return word3

   
    



    
}