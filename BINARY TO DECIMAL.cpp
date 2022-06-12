#include <bits/stdc++.h>

using namespace std;

int main()
{
	string s1;
	cin>>s1;
	int n1 = s1.length();
	int n = 1;
	int sum = 0;
//	cout<<n<<endl;
	for(int i =n1-1; i>=0; --i)
	{
		if( s1[i] == '1')
		{
			sum = sum + n;
		}
		else
		{
			sum = sum +0;
		}
		n = n*2;
	}
	
	cout<<"THE SUM IS "<<sum<<endl;
	
}
