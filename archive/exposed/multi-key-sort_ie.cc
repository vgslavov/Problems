// TODO: compile

using namespace std;

class Employee {
	public:
		string extension;
		string givenname;
		string surname;
};

// TODO: make comparison case insensitive
int
compare(Employee e1, Employee e2)
{
	int ret = e1.surname.compare(e2.surname);

	// surname is the same
	if (ret == 0)
		ret = e1.givenname.compare(e2.givenname);

	return ret;
}

// TODO: give field to compare as arg, make case insensitive comparison
int
cmp_surname(Employee e1, Employee e2)
{
	int ret = e1.surname.compare(e2.surname);

	return ret;
}

int
cmp_givenname(Employee e1, Employee e2)
{
	int ret = e1.givenname.compare(e2.givenname);

	return ret;	
}

void
sort_employees(vector<Employee> employees)
{
	sort(employees.begin(), employees.end(), compare);

	// or sort twice using different keys and a stable_sort()
	// if extra memory: O(n log_2(n))
	// otherwise: O(n log_2^2(n))
	//stable_sort(employees.begin(), employees.end(), cmp_givenname);
	//stable_sort(employees.begin(), employees.end(), cmp_surname);
}