from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.hackernews import HackerNews
from phi.tools.googlesearch import GoogleSearch
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize Google Search Agent with Groq Model
google_search_agent = Agent(
    tools=[GoogleSearch()],

    description="You are a news agent that helps users find the latest news.",
    instructions=[

        "Given a topic by the user, respond with 4 latest news items about that topic.",
        "Search for 10 news items and select the top 4 unique items.",
        "Search in English and in French."
    ],
    show_tool_calls=True,
    debug_mode=True,
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),  # Make sure Groq is used here
)

# Initialize HackerNews Agent with Groq Model
hacker_news_agent = Agent(
    name="Hackernews Team",
    tools=[HackerNews(get_top_stories=True, get_user_details=True)],
    show_tool_calls=True,
    markdown=True,
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview")  # Ensure Groq is used here too
)

# Integrated Agent with Groq Model
integrated_agent = Agent(
    team=[google_search_agent, hacker_news_agent],
    instructions=["Always include sources", "Use table to display data"],
    show_tool_calls=True,
    markdown=True,
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview")  # Ensure Groq is used throughout
)

# Menu-Driven Functionality (updated to remove YouTube tools)
def menu():
    while True:
        print("\n=== Cyber Agent Menu ===")
        print("1. Get Cybersecurity News")
        print("2. Search for Vulnerability and Patch")
        print("3. Perform All Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            # Get cybersecurity news
            topic = input("Enter the topic for cybersecurity news: ")
            try:
                integrated_agent.print_response(
                    f"Search for the latest news on {topic}.", markdown=True
                )
            except Exception as e:
                print(f"Error fetching cybersecurity news: {e}")

        elif choice == "2":
            # Search for vulnerability and patch
            vulnerability = input("Enter the name of the vulnerability: ")
            try:
                integrated_agent.print_response(
                    f"Search for information about {vulnerability} and its patches.",
                    markdown=True,
                )
            except Exception as e:
                print(f"Error fetching vulnerability information: {e}")

        elif choice == "3":
            # Perform all tasks
            topic = input("Enter the topic for cybersecurity news: ")
            vulnerability = input("Enter the name of the vulnerability: ")
            try:
                print("\nFetching cybersecurity news:")
                integrated_agent.print_response(
                    f"Search for the latest news on {topic}.", markdown=True
                )
                print("\nFetching vulnerability information:")
                integrated_agent.print_response(
                    f"Search for information about {vulnerability} and its patches.",
                    markdown=True,
                )
            except Exception as e:
                print(f"Error performing tasks: {e}")

        elif choice == "4":
            # Exit the program
            print("Exiting Cyber Agent. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the menu
if __name__ == "__main__":
    menu()
