#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
    string str;
    cout<<"Enter a string:";
    cin>>str;
    reverse(str.begin(), str.end());
    cout<<str;
}