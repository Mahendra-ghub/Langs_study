#include<iostream>
using namespace std;

int main()
{
    int year;
    cout<<"Enter a year:";
    cin>>year;
    if(year%400==0 && year%100==0 && year%4==0)
       {
        cout<<"leap year"<<endl;
       }
       else if(year%400!=0 && year%100==0 && year%4==0)
       {
        cout<<"not a leap year"<<endl;
       }else if(year%400!=0 &&  year%100!=0 && year%4==0)
       {
         cout<<"leap year"<<endl;
       }else{cout<<"not a year";}
}