class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str : strs){
           sb.append(str.length()).append('#').append(str);
        }
        return sb.toString();
    }
 
    

    public List<String> decode(String str) {
           List<String> list = new ArrayList<>();
           int i = 0;
           while(i < str.length()) {
               int dem = str.indexOf('#', i);
               int length = Integer.parseInt(str.substring(i,dem));
               i = 1+dem;
               list.add(str.substring(i,i+length));
               i += length;

           }
           return list;
    }

}