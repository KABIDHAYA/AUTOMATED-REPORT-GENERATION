# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KABILAN M

*INTERN ID*: CT04CH1571

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH


###  **Task Description: Automated Sales Report Generation using Python**

####  **Objective:**

The goal of this task is to **read a sales dataset**, compute basic statistics, and **generate a professional PDF report** automatically using Python.



###  **Tools & Libraries Used:**

* **`pandas`** – to read and analyze the sales data from `data.csv`
* **`fpdf`** – to create and format the final PDF report
* (Dependencies listed in `req.txt`: `pandas`, `fpdf`)



###  **Steps Performed:**

1. **Data Loading:**

   * Load `data.csv` using `pandas`, which contains records of sales agents, their sales amounts, and regions.

2. **Data Analysis:**

   * Calculate:

     *  Total Sales
     *  Average Sales
     *  Maximum Sale
     *  Top Salesperson

3. **PDF Report Generation:**

   * Create a clean, readable **PDF report (`sales_report.pdf`)** using the `fpdf` library.
   * Include:

     * Report title
     * Total, average, and top salesperson summary
     * Full table of all entries: Name, Sales, Region

4. **Final Output:**

   * Save the file as **`sales_report.pdf`**
   * Print confirmation on the console: `"PDF report generated: sales_report.pdf"`



###  **Example Output:**

From your uploaded PDF, the report looks like this:

* **Total Sales:** 9700
* **Average Sales:** 1940.00
* **Top Salesperson:** Bob (2400)

| Name    | Sales | Region |
| ------- | ----- | ------ |
| Alice   | 1500  | North  |
| Bob     | 2400  | South  |
| Charlie | 1800  | East   |
| Diana   | 2100  | West   |
| Evan    | 1900  | North  |


###  **How to Run This Task:**

1. Make sure you have `data.csv` in the same directory.
2. Install the required libraries:

   ```bash
   pip install -r req.txt
   ```
3. Run the script:

   ```bash
   python app.py
   ```
4. The PDF file `sales_report.pdf` will be created in your current folder.

