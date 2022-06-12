#include <iostream>
#include <cstring>

using namespace std;

bool checkp(char p[])
{
	int n = strlen(p);
	char p1[n];
	int n1 = n -1;
	for (int i = 0; i<n; i++)
	{
		p1[i] = p[n1];
		n1--;
	}
	int k = 0;
	for(int i = 0 ; i<n;i++){
		
		if ( p[i] != p1[i] )
		{
//			cout<<p[i]<<" "<<p1[i]<<" yes" <<endl;
            k++;
		}
		
	}	
	if (k == 0){
		return true;
	}
	else 
	{
	  return false;
	}
	 
	
	
}


int main()
{
	char p[] = "1111";
	if (checkp(p))
	{
		cout<<"true";
	}
	else{
		cout<<" no";
	}
	
}
