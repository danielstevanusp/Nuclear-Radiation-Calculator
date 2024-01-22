the nuclear radiation decay calculator is a python program designed to determine the activity of a radioactive substance at a given time based on its initial activity and half-life. the program utilizes the decay formula:

![image](https://github.com/danielstevanusp/Nuclear-Radiation-Calculator/assets/157248078/06ef60c6-6632-4a76-b0d3-d64c45b988f8)

where:
![image](https://github.com/danielstevanusp/Nuclear-Radiation-Calculator/assets/157248078/7402ecc6-2c6f-483c-a69d-86f4a7ee15ee)

how to use:
1. users are prompted to input the initial radiation activity (a0), time elapsed (t), and the half-life (t1/2).
2. the program calculates the radiation activity using the `calculate_nuclear_radiation` function.
3. the result, representing the radiation activity after the specified time, is displayed in becquerels (bq).

example:
run python3 radiation.py
enter initial activity (bq): 1000.0
enter time (seconds): 3600.0
enter half-life (seconds): 1800.0
nuclear radiation activity after 3600.0 seconds: 500.0 bq

disclaimer: sorry if there are errors and calculations in the code, i'm still learning to improve it.
