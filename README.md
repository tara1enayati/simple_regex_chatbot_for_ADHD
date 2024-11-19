ADHD Chatbot
A simple, regex-based chatbot designed to support individuals with ADHD by providing advice, tips, and empathetic responses. This chatbot offers practical solutions to common ADHD challenges, such as organization, focus, and self-care.

Features
Friendly and empathetic interaction.
Actionable advice for ADHD-specific challenges:
Improving focus and organization.
Managing procrastination and impulsiveness.
Boosting productivity and motivation.
Self-care tips to promote mental health.
Encouraging messages for emotional support.
Built-in responses for a variety of user inputs.
Easy-to-extend regex-based rules for customization.
Technologies Used
Python
Regular Expressions (regex)
How to Use
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/ADHD-Chatbot.git
Navigate to the project directory:

bash
Copy code
cd ADHD-Chatbot
Run the chatbot:

bash
Copy code
python chatbot.py
Interact with the chatbot by typing your queries in the terminal. For example:

User: "Hi"
Chatbot: "Hi there! I’m here to support you. How are you feeling today?"
User: "I struggle with focus"
Chatbot: "Focusing can be tough with ADHD. Try using the Pomodoro technique: work for 25 minutes, then take a 5-minute break."
To end the chat, type exit or quit.

Chatbot Logic
The chatbot operates on a set of predefined regex-based rules. For every user input:

The input is matched against the regex patterns.
If a match is found, the corresponding response is displayed.
If no match is found, the chatbot provides a default response.
The rules are stored in a dictionary, where:

Keys: Regex patterns for user inputs.
Values: Responses the chatbot will return.
Customization
You can customize the chatbot by adding or modifying the regex rules in the rules dictionary in chatbot.py. For example:

Add a new pattern for sleep tips:
python
Copy code
r'(.*) sleep': "Good sleep is essential for ADHD. Try sticking to a consistent bedtime routine and limiting screen time before bed."
Future Enhancements
Integrate natural language processing (NLP) for more nuanced conversations.
Add a GUI for better user interaction.
Connect to external APIs for dynamic responses (e.g., weather, reminders).
Support multilingual conversations.
Contributing
Feel free to contribute to this project by:

Forking the repository.
Making changes or adding features.
Submitting a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
This project was inspired by the desire to provide support and encouragement to individuals living with ADHD. Thank you to the ADHD community for sharing your challenges and solutions, which helped shape the responses in this chatbot.

Feel free to use this chatbot as a starting point for building more advanced conversational agents!
