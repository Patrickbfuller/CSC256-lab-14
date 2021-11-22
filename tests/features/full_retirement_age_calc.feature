Feature: Full Retirement Age Calculator

    As a fiscal person I want to be able to plan my retirement accurately.

    Scenario Outline: Entering an invalid birth year
        Given a new retirement calculator
        When an invalid birth year, "<year>" causes an error

        Examples:
            | year  |
            | 1899  |
            | 2022  |
            | -1990 |

    Scenario Outline: Entering an invalid birth month
        Given a new retirement calculator
        When an invalid birth month, "<month>" causes an error

        Examples:
            | month |
            | 0     |
            | 13    |
            | -1    |

    Scenario Outline: Correct calculation
        Given a new retirement calculator
        When a valid year, "<year>" is entered
        And a valid month, "<month>" is entered
        Then the retirement age should be "<years>" years and "<months>" months
        And the retirement date should be month "<ret month>" of year "<ret year>"

        Examples:
            | year | month | years | months | ret month | ret year |
            # Minimum values
            | 1900 | 1     | 65    | 0      | 1         | 1965     |
            # Maximum values
            | 2021 | 12    | 67    | 0      | 12        | 2088     |
            # Equivalency groups for different retirement ages
            | 1937 | 9     | 65    | 0      | 9         | 2002     |
            | 1938 | 9     | 65    | 2      | 11        | 2003     |
            # Also covers rolling over months to following year
            | 1939 | 9     | 65    | 4      | 1         | 2005     |
            | 1940 | 9     | 65    | 6      | 3         | 2006     |
            | 1941 | 9     | 65    | 8      | 5         | 2007     |
            | 1942 | 9     | 65    | 10     | 7         | 2008     |
            | 1943 | 9     | 66    | 0      | 9         | 2009     |
            | 1954 | 9     | 66    | 0      | 9         | 2020     |
            | 1955 | 9     | 66    | 2      | 11        | 2021     |
            | 1956 | 9     | 66    | 4      | 1         | 2023     |
            | 1957 | 9     | 66    | 6      | 3         | 2024     |
            | 1958 | 9     | 66    | 8      | 5         | 2025     |
            | 1959 | 9     | 66    | 10     | 7         | 2026     |
            | 1960 | 9     | 67    | 0      | 9         | 2027     |
