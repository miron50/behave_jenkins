@tags @hmtask
Feature: hmtask
    Scenario: Run with server 'localhost:2222' and 'd:\1test\test.txt' as output file
        Given Type 'localhost' as Server Address
        And Type '2222' as Server Port
        And Type 'd:\1test\test.txt' as output file
            When Launch client
            Then Output file exists with information


    Scenario: Run with invalid server address
        Given Type '255.255.255.255' as Server Address
        And Type '2222' as Server Port
        And Type 'd:\1test\test.txt' as output file
            When Launch client
            Then Connect with 'WinError 10049'


    Scenario: Run with invalid server port
        Given Type 'localhost' as Server Address
        And Type '1234' as Server Port
        And Type 'd:\1test\test.txt' as output file
            When Launch client
            Then Connect with 'WinError 10061'


    Scenario: Run without output file
        Given Type 'localhost' as Server Address
        And Type '1234' as Server Port
            When Launch client
            Then Connect with 'BDD_Task: error: the following arguments are required: -o/--output'