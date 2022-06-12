#include <bits/stdc++.h>

using namespace std;

void func(char a[], char a1[])
{
	string k(a);
	string k1(a1);
	cout<<k<<endl;
	cout<<k1<<endl;
	sort(k.begin(), k.end());
	sort(k1.begin(), k1.end());
	if(k == k1)
	{
		cout<<"it is"<<endl;
	}
	else
	{
		cout<<"it is not"<<endl;
	}
//	cout<<"k "<<k<<endl;
//	cout<<"k1 "<<k1<<endl;
	
}

int main()
{
	char a[]="hello world";
	char a1[]="hello world";
	func(a, a1);
}
