import java.util.*;
    public class main {
       
    	public void getdata() {
    		Scanner s2=new Scanner(System.in);
    		Random random= new Random();
    		int n=random.nextInt(9)+1;
    		int temp=n*785;
    		System.out.print("\nOTP IS:"+temp);
    		int op;
    		System.out.print("\nEnter the OTP sent to your linked Gmail:");
    		int op1=s2.nextInt();
    		s2.nextLine();
    		if(op1==temp)
    		{
    			System.out.print("\nEnter the new password:");
    			String pass2=s2.nextLine();
    			System.out.print("\nConfirm your password:");
    			String pass3=s2.nextLine();
    			System.out.println("\nPassword changed succesfully! Welcome back chief!");
    		}
    	}
    	public void putdata()
    	{
    		System.out.println("\nRefresh your home page and try again!");
    	}
	public static void main(String[] args) {
		String acc;
		String pass;
		int ch=0;
		main obj=new main();
		Scanner s=new Scanner(System.in);
		System.out.print("\nEnter the username:");
		acc=s.nextLine();
		System.out.print("\nEnter the password:");
		pass=s.nextLine();
		boolean Z;
		if(Z=acc.isEmpty())
		{
			boolean X;
			if(X=pass.isEmpty())
			{
				System.out.print("\nYou have entered the wrong username and password!");
				System.out.print("\nFORGOT PASSWORD\n1.yes 2.no");
				System.out.print("\nEnter your choice:");
				ch=s.nextInt();
				if(ch==1)
				{
					obj.getdata();
				}
			}
		}
		
              if(ch==2)
              {
            	  obj.putdata();
              }
              else
              {
            	  System.out.println("\nWELCOME BACK CHIEF!");
              }
	}

}
