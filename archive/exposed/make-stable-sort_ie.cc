// O(n + n log(n)) = O(n log(n))
// assign seq #: O(n)
// additional mem: O(n)

using namespace std;

class Employee {
	public:
		string extension;
		string givenname;
		string surname;
		int seq;
};

void
stable_sort(vector<Employee> employees)
{
	for (int i = 0; i < employees.length(); i++) {
		emplyees[i].seq = i;
	}
	shakySort(employees, compare);
}

// tie breaker
// TODO: make comparison case insensitive
int
compare(Employee e1, Employee e2)
{
	int ret = e1.surname.compare(e2.surname);

	// make stable
	if (ret == 0)
		ret = e1.seq - e2.seq;

	return ret;	
}