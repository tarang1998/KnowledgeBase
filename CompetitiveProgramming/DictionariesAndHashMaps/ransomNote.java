import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'checkMagazine' function below.
     *
     * The function accepts following parameters:
     *  1. STRING_ARRAY magazine
     *  2. STRING_ARRAY note
     */

    public static void checkMagazine(List<String> magazine, List<String> note) {
        // Write your code here
      HashMap<String, Integer > magazineDictionary = new HashMap<>();

        for(int i = 0; i < magazine.size(); i++){
            if(magazineDictionary.containsKey(magazine.get(i))){
                int wordCount = magazineDictionary.get(magazine.get(i));
                magazineDictionary.put(magazine.get(i), wordCount+1);
            }
            else{
                magazineDictionary.put(magazine.get(i),1);
            }
        }

        for(int i = 0 ; i< note.size(); i++){

            if(magazineDictionary.containsKey(note.get(i))){

                int wordCount = magazineDictionary.get(note.get(i));
                if(wordCount == 0){
                    System.out.println("No");
                    return;
                }
                else{
                    magazineDictionary.put(note.get(i),wordCount-1);
                }
            }
            else{
                System.out.println("No");
                return;

            }
        }
        
        System.out.println("Yes");


    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int m = Integer.parseInt(firstMultipleInput[0]);

        int n = Integer.parseInt(firstMultipleInput[1]);

        List<String> magazine = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .collect(toList());

        List<String> note = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .collect(toList());

        Result.checkMagazine(magazine, note);

        bufferedReader.close();
    }
}
