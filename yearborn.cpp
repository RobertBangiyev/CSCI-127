//Robert Bangiyev
//November 26, 2018
//This program asks user for numbers and does which year is bigger or something like that
#include <iostream>
using namespace std;

int main()
{
    int birth;
    cout << "Please enter year born: ";
    cin >> birth;
    
    if(birth>2018)
        while(birth>2018)
        {
            cout << "Entered a future year\n";
            cout << "Please enter year born: ";
            cin >> birth;
        }
    cout << "You entered: ";
    cout << birth;
    return 0;
}
