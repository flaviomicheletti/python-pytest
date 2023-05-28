# Decorators

**mark:** It allows you to mark test cases with specific attributes, such as 
marking them as skipped, expected to fail, or only running them under certain 
conditions. For example: @pytest.mark.skip, @pytest.mark.xfail. 

**fixture:** It is used to define fixtures, which are functions that provide 
a set of data or resources to be used by one or more test cases. Fixtures are 
typically used for setup and teardown operations. For example: 
@pytest.fixture. 

**parametrize:** It allows you to define multiple sets of input values for a 
test function using parameterization. It helps in running the same test code 
with different inputs. For example: @pytest.mark.parametrize. 

**raises:** It is used to specify the expected exception that a test function 
should raise. It helps in testing exception handling. For example: 
@pytest.raises. 

**skip:** It is used to skip a test case. You can use it to temporarily 
exclude certain tests from being executed. For example: @pytest.mark.skip. 

**xfail:** It is used to mark a test case as expected to fail. It is useful 
when you want to run a test case that is currently failing but should pass in 
the future. For example: @pytest.mark.xfail. 

**fixture_scope:** It specifies the scope of a fixture. The available scopes 
are function (default), class, module, and session. It determines how often 
the fixture is invoked during the test run. 



## @pytest.mark

**@pytest.mark.parametrize:** This decorator allows you to define 
parametrized tests, where a test function is executed with different sets of 
input parameters. 

**@pytest.fixture:** Used to define fixtures, which are functions that 
provide test resources or set up and tear down test environments. 

**@pytest.mark.skip:** Skips the decorated test or test function, allowing 
you to temporarily exclude specific tests from execution. 

**@pytest.mark.skipif:** Skips the test or test function based on a specific 
condition or expression, allowing conditional skipping of tests. 

**@pytest.mark.xfail:** Marks a test as expected to fail, either due to known 
issues or as a placeholder for future development. 

**@pytest.mark.parametrize_with_cases:** A powerful decorator for creating 
parametrized tests using reusable test cases defined in separate functions or 
classes. 

**@pytest.mark.timeout:** Applies a timeout to the decorated test or test 
function, terminating its execution if it exceeds the specified time limit. 

**@pytest.mark.usefixtures:** Explicitly specifies which fixtures should be 
used by a test or test function, overriding any automatic fixture discovery. 

**@pytest.mark.parametrize("arg", value):** A variant of the 
@pytest.mark.parametrize decorator that allows you to specify the parameter 
name using a string instead of a function argument. 

**@pytest.mark.filterwarnings:** Filters or modifies warning messages during 
test execution, allowing you to suppress or handle warnings in specific 
tests. 

**@pytest.mark.dependency:** Defines dependencies between tests, ensuring 
that tests are executed in a specific order based on their dependencies. 

**@pytest.mark.flaky:** Marks a test as flaky, meaning it may fail 
intermittently but should be retried a specified number of times before being 
marked as a failure. 

**@pytest.mark.run:** Controls the execution of specific tests based on 
command-line options or custom expressions, allowing fine-grained control 
over test selection. 

**@pytest.mark.parametrize_with_cases:** Combines parameterization and test 
case management by defining parametrized tests using reusable test cases 
defined in separate functions or classes. 

**@pytest.mark.slow:** Identifies tests that are slow to execute, helping you 
prioritize or separate them from regular tests during test runs. 


