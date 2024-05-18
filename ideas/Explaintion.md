# Test Approach

This is a UI test framework wrote by Selenium and Python and using the design pattern POM.
<br>

# Test Cases
1.  Check if all urls is valid, including external and internal
2. Check if Navigation buttons works as desired
3. Validate the functionality of Vocabulary section

# Assumptions
Only need to test the element of the subject page.
Navigation bar, Aside page and Footer test cases should be elsewhere

# Project Struct
1. Each functionally is break into page object which is located in pages
2. Utilities contains methods that using to write/read files
3. Tests cases are under tests
4. Reports contains test result in html format
5. Logs