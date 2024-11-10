/*#include<iostream>
using namespace std;

int main()
{
    char c;
    cout<<"enetr a letter:";
    cin>>c;
    if(c=='a'|| c=='e' || c=='i' ||c=='o' || c=='u')
    {
        cout<<"vowel"<<endl;
    }else{
        cout<<"constonant"<<endl;
    }

}*/

#include<iostream>
using namespace std;

int main()
{
    char c;
    cout<<"enetr a letter:"<<endl;
    cin>>c;

    switch(c){
    case 'a':
       cout<<"vowel"<<endl;
        break;
    
    case 'e':
        cout<<"vowel"<<endl;
        break;

    case 'i':
       cout<<"vowel"<<endl;
       break;

    case 'o':
       cout<<"vowel"<<endl;
       
    default:
       cout<<"consonant"<<endl;
    }
}