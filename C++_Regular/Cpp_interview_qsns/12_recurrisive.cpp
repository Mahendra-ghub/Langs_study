#include<iostream>
using namespace std;

int work(int e, int f)
{
    if(e<f)
    return work(f,e); //swapping of values recurrisive function activated __f=8     e=7

    else if(f!=0)
    return e+work(e,f-1);

    else
    return 0;
}

int main()
{
    int e=7;
    int f=8;
    cout<<"result:"<< work(e,f);
}