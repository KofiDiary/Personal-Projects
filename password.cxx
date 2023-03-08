# include <iostream>
using namespace std;

int main ()
{
	int Password = 2564;
	int Password1;
	int Number = 0;
	int loop;
	cout << "Welcome to Diary.app" << "\nPlease Enter Your Password To Proceed: ";
	cin >> Password1;
	loop = true;
	while (loop)
	{
		
		if (Password1 != Password && Number < 3)
		{
			cout << "You've entered the wrong password" << "\nRe-enter your password: ";
			cin >> Password1;
			Number = Number + 1;
			if (Password1 == Password)
			{
				cout <<"You've entered the right password";
				break;
			}
			
			else
			{
				Number = Number + 1;
				if (Password != Password1 && Number > 3)
				{
					cout <<"Too many failed attempts, your account has been blocked";
					break;
				}
			}
			
		}
		
		else
		{
			cout <<"You've entered the right password";
			break;
		}
	}
}