/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		for(int i=0;i<t;i++)
		{
		    int n=sc.nextInt();
		    int a[]=new int[n];
		    for(int j=0;j<n;j++)
		    {
		        a[j]=sc.nextInt();
		    }
		    Map<Integer,Integer> d=new HashMap<>();
		    List<Integer> list = new ArrayList<>();
		    for(int x:a)
		    {
		        d.put(x,d.getOrDefault(x,0)+1);
		        list.add(x);
		    }
		    Collections.sort(list,(l1,l2)->{
		        int f1=d.get(l1);
		        int f2=d.get(l2);
		        if (f1 != f2) 
		        {
		            return f2-f1;
		        }
		        else
		        {
		            return l1-l2;
		        }
		    });
		    for(int j=0;j<list.size();j++)
            {
                System.out.print(list.get(j)+" ");
            }
            System.out.println();
		}
	}
}