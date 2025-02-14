<h1 align="center">Documentation</h1>
<div align="center">
    <a href="/README.md">English</a>
    <a href="/README_ru.md">Русский</a>
    <br><br>
    <img src="https://github.com/user-attachments/assets/9b694a20-7473-4ab5-a972-edda0c085de2" align="center" width="400" height="200" />
    <img src="https://github.com/user-attachments/assets/86685579-d395-4c09-860b-9082a397921a" align="center" width="400" height="200" />
</div>

## Usage

1. Install require modules

    ```sh
    python -m pip install -r requirements.txt
    ```
    
2. Start app

    ```sh
    python app.py
    ```
    
3. Choice options (for quite input 0)

    - If you choice first option: 

        1.  Input phone number and duration action(sec) through space

            ```python
            +89999999999 60
            ```
            
    - Else if you choice second option:

        1. Input number of option (1-8). This is reason for report
        
        2. Input username
        
        3. Input Telegram ID
        
        4. Input count reports
        
## Description 

This code represents an implementation of a utility for launching DoS attacks on phone numbers using methods such as SMS, calls, and feedback requests. The program integrates multiple services to execute these attacks while managing requests asynchronously to enhance operational efficiency.

## Imported Modules

1. **`Attack.Services` and `Attack.Feedback_Services`**: Modules containing functions and data with addresses of websites that offer SMS bomber services. These modules provide the necessary information for executing the attacks.
2. **`time`, `os`, `requests`**: Standard Python libraries used for managing delays, interacting with the operating system (e.g., for module installation), and performing HTTP requests.
3. **`asyncio`**: A library for asynchronous programming that allows multiple tasks to run simultaneously without blocking.
4. **`Attack.functions`**: Helper functions for user interaction, such as controlling text color in the console, clearing the terminal, animating messages, and system management.

## Classes and Objects

- **`Color`**: A class for managing text color in the terminal, enabling users to visually distinguish different messages.
- **`System`**: A class for handling system values and parameters related to the program's operation.

## Main Program Code

1. **Internet Connection Check**: The program starts by checking for internet access. If there is no access, it terminates with an appropriate message.

2. **Update Check**: The utility checks for updates for the current version of the program.

3. **Import Necessary Libraries**: The program attempts to import the `keyboard` and `aiohttp` libraries, which are essential for its operation. If they are not installed, the user is given the opportunity to install them automatically.

4. **Phone Number and Duration Input**: The user inputs a phone number and the desired duration for the attack. The program processes these inputs and verifies their correctness. If the input data is valid, execution continues.

5. **Asynchronous Attacks**:
    - Several main asynchronous functions are defined:
      - **`request`**: A function to execute requests to services and track successful and unsuccessful attempts. It sends HTTP requests to the selected services while keeping track of the attack duration.
      - **`async_attacks`**: A function to handle multiple services within a single attack, calling `request` for each service.
      - **`run_attacks`**: A function for managing the attack duration, allowing multiple executions of `async_attacks` until the specified attack period elapses.

6. **Displaying Results**: After the attack concludes, the program displays the results, including:
   - Total duration of the attack.
   - Number of successfully processed requests.
   - Number of failed attempts.

7. **Exception Handling**: The program contains handlers for various errors, including invalid phone numbers and user interruptions via keyboard. This helps the program remain resilient to crashes and respond appropriately to errors.

## Conclusion

This code serves as an example of a utility for executing SMS bomber attacks using asynchronous programming for improved performance. A critical aspect of the implementation is the validation of input data and the capability for automatic module installation, enhancing user convenience. However, it is important to note that using such utilities is unethical and may be illegal depending on the jurisdiction.
