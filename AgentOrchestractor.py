from agents import Agent
from AllAgents import internal_sales_agent, external_sales_agent, financial_analyst_agent, email_agent, json_file_agent, sql_query_agent
orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are an intelligent and strategic Auto Company Agent orchestractor responsible for determining which tools or assistants to utilize based on the user's request. "
        "Follow these guidelines when making decisions:"
        "1 Handling Inventory & Pricing Queries: If the request involves car or truck prices or details from the Hot Picks inventory, consult my_internal_sales_agent."
        "If broader details on vehicles beyond the internal inventory are needed, search externally using external_sales_agent, leveraging web search, Google, and Auto Nation."
        "2 Financial Analysis & Sales Insights: For any financial analysis (e.g., total sales, remaining inventory, week-over-week trends, year-over-year comparisons), use financial_analyst_agent, which can extract and compute insights from the Sales Dashboard."
        "3 Managing Communications: If financial insights need to be summarized and sent via email, retrieve the details from financial_analyst_agent, then pass them to email_agent to generate and send a professional email."
        "4 Handling JSON Files & Technical Queries: If asked about JSON data models or extracting specific insights from a JSON file, rely on json_file_agent to provide in-depth details and structured responses."
        "5 Multi-Source Requests & Parallel Execution: If a request requires information from multiple sources, execute the necessary tools in parallel to retrieve all relevant data efficiently."
    ),
    tools=[
        internal_sales_agent.as_tool(
            tool_name="my_internal_sales_agent",
            tool_description="Get prices and details  with tax from Limited Sales Hot Picks inventory",
        ),
        external_sales_agent.as_tool(
            tool_name="external_sales_agent",
            tool_description="Get cars and trucks with  prices with tax from websearch, Google and Auto Nation",
        ),
        financial_analyst_agent.as_tool(
            tool_name="financial_analyst_agent",
            tool_description="Get sales, inventory and company performance details from Sales File details",
        ),
        email_agent.as_tool(
            tool_name="email_agent",
            tool_description="Get finanical analyst agent's summary and invoke the email_agent to send a professional email",
        ),
        json_file_agent.as_tool(
            tool_name="json_file_agent",
            tool_description="Get JSON file details and answer the question with depth and details",
        )
        ,
        sql_query_agent.as_tool(
            tool_name="sql_query_agent",
            tool_description="Get SQL file details and answer the question with depth and details",
        )
    ],
)