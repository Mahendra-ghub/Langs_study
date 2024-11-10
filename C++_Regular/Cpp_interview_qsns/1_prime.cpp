#include<iostream>
using namespace std;

bool isprime(int n)
{
    if (n<=1) return false;

      for (int i =2; i<=n/2; i++)
       {if (n%i == 0) return false;}

    return true;
}


int main()
{
    int n = 7;
    if (isprime(n))
      cout<<n<<"is a prime numeber";
    else
    {
        cout<<n<<"is not a prime number:";
    }

}