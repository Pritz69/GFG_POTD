def maxArea(a,le):
    #code here
    ans=0
    i=0
    j=le-1
    while i<j :
        ans=max(ans,min(a[i],a[j])*(j-i))
        if a[i]<a[j] :
            i +=1
        else :
            j -=1
    return ans
