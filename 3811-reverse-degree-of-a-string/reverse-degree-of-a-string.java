class Solution {
    public int reverseDegree(String s) {
        int sum=0;
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            int ascci=(int) ch;
            sum+=((int)'z'-ascci+1)*(i+1);

        }
        return sum;
        
    }
}