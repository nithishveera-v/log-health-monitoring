# Log Health Monitoring Utility (Python)

## Overview
This project is a lightweight Python-based backend utility that analyzes system log files and generates a structured summary report.

It demonstrates fundamental log analysis concepts commonly used in real-world IT operations, system monitoring, and backend diagnostics.

The project focuses on clarity, correctness, and practical relevance rather than scale or automation.

## Problem Statement
System log files often contain large volumes of unstructured text.  
Manually identifying critical issues such as errors, warnings, or repeated login failures is time-consuming and error-prone.

This project provides a simple and reliable approach to analyze such logs and extract meaningful insights.

## Solution
The utility processes a log file line by line and detects predefined patterns such as:
- Errors  
- Warnings  
- Failed login attempts  

Based on configurable thresholds, it highlights potential operational or security concerns and writes the results to a summary report file.

## Key Features
- Plain-text log file processing  
- Case-insensitive pattern matching  
- Configurable alert thresholds  
- Automatic summary report generation  
- Graceful handling of missing files  

## Technologies Used
- Python 3  
- Standard Python libraries (file handling, exception handling)

## How to Run
1. Place the log file in the project directory (input_logs.txt)
2. Run the Python script:

```bash
python log_file.py
```

3. Review the generated summary report (`summary_report.txt`)

## Repository Structure


```md


log-health-monitoring/
├── log_file.py
├── input_logs.txt
├── Log_Health_Monitoring_Project_Report.pdf
├── README.md
├── LICENSE
└── .gitignore
