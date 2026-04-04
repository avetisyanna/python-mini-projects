# Thread Shed

## Description
Thread Shed is a Python project that helps a sewing hobby shop keep track of daily sales. The shop has an old register system that saves all the sales information in one long string called `daily_sales`. Each sale has:

- The customer’s name  
- The amount of money they spent  
- The types of thread they bought  
- The date of the sale

This project shows how to use Python to:

- Organize the sales information into separate lists  
- Find out how much money was made in total  
- Count how many threads of each color were sold  
- Keep track of customer names  

---

## How it works
1. The program starts with the big `daily_sales` string.  
2. It cleans up the string and separates it into individual sales.  
3. For each sale, it saves:  
   - The customer’s name in a list called `customers`  
   - The amount they spent in a list called `sales`  
   - The threads they bought in a list called `thread_sold`  
4. If a sale has more than one color of thread, it separates them so each color can be counted.  
5. It adds up all the money from the `sales` list to get the total sales.  
6. It counts how many threads of each color were sold and prints the results.

---

## How to run
1. Clone the repository:

```bash
git clone https://github.com/avetisyanna/Thread-Shed.git
