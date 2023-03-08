# include <iostream>
using namespace std;

int main()
{
	int Password1 = 2564;
	int loop;
	int Password;
	int Number = 0;
	cout << "Welcome to Diary Bank" << "\nEnter Your Pin To Proceed: ";
	cin >> Password;
	if (Password != Password1 && Number < 4)
	{
		loop = true;
		while (loop)
		{
			cout << "You've entered the wrong password";
			cout << "\nRe-enter password: ";
			cin >> Password;
			Number = Number + 1;
			if (Password == Password1)
			{
				cout << "You've entered the right password";
				break;
			}
		}
	}
	else if (Password != Password1 && Number > 3)
	{
		cout << "Too many failed attempts, your account has been blocked";
	}
	else
	{
		cout << "You've entered the right password";
	}
}