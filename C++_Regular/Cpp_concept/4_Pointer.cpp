#include<iostream>
using namespace std;

void fun(int* ptr)
{
    *ptr = 10;
}

int main()
{
    int x = 20;
    fun(&x);
    cout<<"fun value is:"<<x<<endl;
}