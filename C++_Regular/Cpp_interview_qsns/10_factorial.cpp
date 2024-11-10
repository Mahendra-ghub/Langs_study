#include<iostream>
using namespace std;

int main()
{
    int n;
    int f;
    cout<<"enter a number:";
    cin>>n;
    f=n;
    for(int i=1;i<=n;i++)
    {
        cout<<f<<"*"<<i<<"=";
        f=f*i;
        cout<<f<<endl;
        
    }
     
}