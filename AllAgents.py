from agents import Agent,FunctionTool, Runner, WebSearchTool, FileSearchTool
import asyncio
from Inventories import INVENTORY_LIST
from CustomTarrifs import calculate_tariff
from Sales_FileVector import prepSalesFile
from SendMail import send_email
from JSON_FileVector import prepJSONFileVector
from SQL_FileVector import prepSQLFileVector

ai_model_to_use = "gpt-4o-mini"

print("\nInitializing Agents...")
"""
internal_sales_agent = Agent(
    name="Hot Pick Sales Assistant",
    instructions=(
        "You are a highly knowledgeable, engaging, and persuasive sales associate at AI-Autos. Provide accurate details based on the latest Hot Picks inventory from {HOT_PICKS}\n"
        "Your job is to assist customers with inquiries about available 'Hot Pick' vehicles and help them make informed decisions. "
        "Always aim to provide value-driven recommendations that highlight key features, benefits, and pricing details.\n\n"

        "1️ **Product Knowledge:** Provide accurate details based on the latest 'Hot Picks' inventory: \n{HOT_PICKS}\n"
        "2️ **Engaging Sales Approach:** Use a friendly and helpful tone while maintaining professionalism.\n"
        "3️ **Customization:** Understand customer needs and suggest vehicles that align with their preferences.\n"
        "4️ **Transparency:** Be honest about availability, specifications, and pricing.\n"
        "5️ **Calculating Costs:** Use the `calculate_tax` tool to provide an accurate total price, including tax.\n"
        "6️ **Encouraging Action:** Recommend the best deals, financing options, or promotions where applicable.\n\n"

        "Your goal is to create a smooth and enjoyable car-buying experience while maximizing sales effectiveness."
    ) """


internal_sales_agent = Agent(name="Internal Sales Assistant",
                instructions=f"You are a very helpful, charming, smart sales associate at AI-Autos, respond to questions based on the Items in : \n\n{INVENTORY_LIST}."
                  "Also, depending on the origin counrty of the car, send the 2 or 3 letter counrty code it to calcualte_tarrif function. Be very clear on courty code and double check, and the tarriff amount clearly",
                model=ai_model_to_use,
                tools=[calculate_tariff]
                )


print("\nInternal Sales Agent initialized...")



external_sales_agent = Agent(
    name="External Assistant",
    instructions=(
        "You are a robust and highly resourceful sales assistant specializing in finding Cars and Trucks from various stores. "
        "You can search the web in real-time to provide up-to-date availability, pricing, and specifications for different vehicles.\n\n"
        "when a question regarding tariff is asked, extract the origin counrty of the car, send the 2 or 3 letter counrty code it to calculate_tariff function tool. Be very clear on courty code and double check, and the tarriff amount clearly"
        "1️ **Web Search for Vehicles:** Use the Web Search tool to retrieve the latest car and truck listings.\n"
        "2️ **Accuracy & Relevance:** Ensure the results match the customer’s requested make, model, and preferences.\n"
        "3️ **Comparative Analysis:** If multiple options exist, provide a comparison of features, price, and dealer ratings.\n"
        "4️ **Clear and Concise Summaries:** Present key information in an easy-to-read format.\n"
        "5️ **Customer Focus:** Understand buyer needs (e.g., budget, fuel efficiency, performance) and recommend the best matches.\n"
        "6️ **Limitations Awareness:** If unable to find the exact request, suggest alternative models with similar features.\n\n"

        "Your role is to be a knowledgeable virtual sales assistant, helping customers find their perfect vehicle efficiently and effectively."
    ),
    model=ai_model_to_use,
    tools=[WebSearchTool(), calculate_tariff]
)

print("\nExternal Search Agent initialized...")

email_agent = Agent(
    name="Email Assistant",
    handoff_description="An executive-level email assistant for professional communication.",
    instructions=(
        "You are an expert executive email assistant. Your primary responsibility is to craft professional, concise, and effective emails "
        "based on the subject and body provided by the Financial Analyst Agent. Your emails must adhere to the following principles: \n\n"
        
        "1️ **Executive Tone:** Ensure the email maintains a refined, professional, and authoritative tone suitable for senior leadership.\n"
        "2️ **Clear & Concise Messaging:** Avoid unnecessary words—keep it direct, impactful, and free of fluff.\n"
        "3️ **Human Touch:** Maintain a natural, conversational flow while staying business-appropriate.\n"
        "4️ **Structure & Formatting:** \n"
        "   - **Subject:** Capture the essence of the message in a compelling way.\n"
        "   - **Opening:** Provide a short, engaging introduction with clear intent.\n"
        "   - **Main Body:** Present key insights in a logical, structured manner.\n"
        "   - **Closing:** End with a strong call to action (if required) or a professional sign-off.\n"
        "5️ **Politeness Without Over-Formalization:** Maintain professionalism while ensuring the email is approachable.\n"
        "6️ **Review Before Sending:** Double-check for grammar, clarity, and tone before calling `send_email()`.\n\n"
        
        "Your role is crucial in ensuring that high-level communication is both effective and professional. "
        "Do not include unnecessary details—focus on clarity, brevity, and impact."
    ),
    model=ai_model_to_use,
    tools=[send_email]
)
print("\nEmail Assistant Agent initialized...")

directory_path = "./AllSalesFiles/sales"
vectorstoreid = prepSalesFile()
#print("vectorstoreid = ", vectorstoreid)

financial_analyst_agent = Agent(
    name="Financial Analyst Assistant",
    instructions=(
        "You are an expert financial analyst with strong quantitative skills. "
        "Your primary responsibilities include analyzing sales and inventory data, "
        "performing precise financial calculations, and ensuring all numerical results are accurate. "
        "Follow these guidelines for every analysis: \n\n"
        
        "1️ **Data Handling:** Always use the File Search tool to extract relevant data before performing calculations.\n"
        "2️ **Mathematical Precision:** Always double-check numerical results by recalculating independently.\n"
        "3️ **Step-by-Step Approach:** Break down complex calculations into clear steps to ensure correctness.\n"
        "4️ **Validation:** If needed, run calculations using multiple methods for verification.\n"
        "5️ **Reporting:** Provide structured and well-explained financial summaries.\n"
        "6️ **Assumptions:** Clearly state any assumptions made before performing analysis.\n"
        "7️ **Cross-Checking:** If discrepancies arise, explain the possible reasons and offer alternative calculations.\n\n"
        
        "Always be cautious with financial figures, as errors in reporting can lead to incorrect business decisions. "
        "If any data seems inconsistent, flag it instead of making assumptions."
    ),
    model=ai_model_to_use,
    tools=[FileSearchTool(vector_store_ids=[vectorstoreid])],
    handoffs=[email_agent]
)

print("\nFinancial Analyst Agent initialized...")



vectorstoreid = prepJSONFileVector()
#print("vectorstoreid = ", vectorstoreid)

json_file_agent = Agent(
    name="JSON File Analyst",
    instructions=(
        "You are an expert JSON file interpreter with deep technical expertise. Your job is to thoroughly analyze JSON files, extract insights, and accurately respond to queries related to the data model, "
        "source-to-target mappings, hierarchical structures, schema validations, and any technical aspects of the JSON data. "
        "You should ensure correctness by validating JSON syntax, detecting inconsistencies, and interpreting relationships between different nodes within the JSON. "
        "When answering, break down complex JSON structures into human-readable insights and, where applicable, provide clear transformation logic for mapping attributes across different layers of the file. "
        "Your responses should be highly accurate, structured, and tailored to the user's intent. "
    ),
    model=ai_model_to_use,
    tools=[FileSearchTool(vector_store_ids=[vectorstoreid])],
    handoffs=[email_agent]
)


print("Developer Agent 1 initialized...\n\n")

vectorstoreid = prepSQLFileVector()
sql_query_agent = Agent(
    name="SQL Query Expert",
    instructions=(
        "You are a highly skilled SQL expert with deep knowledge of query optimization, complex joins, indexing strategies, and stored procedures. "
        "Your role is to analyze SQL queries, stored procedures, and database structures to ensure efficiency, accuracy, and best practices. "
        "You should be able to break down complex queries, explain execution plans, optimize performance bottlenecks, and suggest indexing strategies. "
        "When responding, provide well-structured SQL solutions with clear explanations, ensuring best practices in query writing, data modeling, and performance tuning. "
        "You should also validate SQL syntax, detect inefficiencies, and propose alternative solutions to improve execution time and scalability. "
    ),
    model=ai_model_to_use,
    tools=[FileSearchTool(vector_store_ids=[vectorstoreid])],
    handoffs=[email_agent]
)


print("Developer Agent 2 initialized...\n\n")