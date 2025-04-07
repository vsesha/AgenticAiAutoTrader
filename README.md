
# **Agentic AI in Action: AUTO-Trader Powered by OpenAI's Agent SDK  **  

## **Overview**  
This application leverages **OpenAI's Agent SDK** and a suite of specialized AI agents to support various tasks, including **File Search, Web Search, Tools Integration, Handoffs, and Developer Efficiency Agents**. It enhances sales assistance, financial analysis, and code/documentation generation for structured files like JSON and SQL stored procedures.  

### **Project Purpose**  
This application serves as a hands-on exploration of OpenAI's Agent SDK in real-world use cases. While functional, there are opportunities for improvement—particularly in optimizing `*.FileVector.py` to handle multiple files within a directory. Future enhancements will focus on refining this capability, making it a key aspect of the project's evolution.


## **Key Features**  
✅ **Sales Agents** – Assist with internal and external vehicle sales using inventory data and live web searches.  
✅ **Financial Analyst Agent** – Performs detailed financial calculations using File Search.  
✅ **Email Assistant** – Crafts professional, executive-level emails.  
✅ **Developer Efficiency Agents:**  
- JSON File Analyst – Extracts data models, mappings, and insights.  
- SQL Query Expert – Analyzes stored procedures, optimizes queries, and provides best practices.  

## **Agents and Capabilities**  

### 🚗 **Sales Agents**  
1. **Internal Sales Agent** – Assists with car sales from a predefined inventory list.  
2. **External Sales Agent** – Searches the web in real-time for available vehicles.  

### 📊 **Business Intelligence & Financial Agents**  
3. **Financial Analyst Agent** – Analyzes sales/inventory data, validates calculations, and ensures reporting accuracy.  

### ✉️ **Communication Agents**  
4. **Email Assistant** – Helps in crafting high-quality executive emails.  

### 🛠 **Developer Efficiency Agents**  
5. **JSON File Analyst** – Extracts metadata, relationships, and documentation from JSON files.  
6. **SQL Query Expert** – Reviews and optimizes SQL queries, stored procedures, and indexing strategies.  

## **Tools & Handoffs**  
- **File Search** – Extracts structured data from stored files.  
- **Web Search** – Retrieves live information from the internet.  
- **Tax Calculation Tool** – Computes final vehicle pricing, including tax.  
- **Email Handoff** – Automates sending well-structured emails.  

## **Setup & Execution**  

### **1. Prerequisites**  
- Python **3.8+**  
- Required dependencies (install via pip):  
  ```bash
  pip install openai-agents
  pip install python-dotenv
  ```

### **2. API Key and Configuration**  
* Open API account:
- Create your account with Open API platform: https://platform.openai.com/
- For Open API integration, you must have a minimum balance ($5)

* Ensure you have a valid OpenAI API key stored in `.env`:  
```txt
OPENAI_API_KEY=your_api_key_here
```

### **3. Running the Application**  
Execute the script:  
```bash
python AutoAiTrader.py
```
###**4. SMTP/Email configuration**
In this application I use SMTP libraries to send email. Make sure to set the following environment variables
```txt
  SENDER_EMAIL_ID
  SENDER_EMAIL_PWD 
```
also if you are using Gmail, enable App Password for authentication.
Follow instructions: https://support.google.com/accounts/answer/185833?hl=en
