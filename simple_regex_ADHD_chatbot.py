rules = {
    # Greetings and Basic Interaction
    r'hi|hello|hey': 'Hi there! I’m here to support you. How are you feeling today?',
    r'how are you': 'I’m doing well, thank you! More importantly, how are you feeling?',
    r'(who|what) are you': 'I’m your friendly chatbot, here to share tips and advice for living with ADHD.',

    # ADHD-specific Challenges
    r'i (struggle with|have trouble with|can not) focus': (
        "Focusing can be tough with ADHD. Try using the Pomodoro technique: work for 25 minutes, then take a 5-minute break."
    ),
    r'i (can\'t|cannot|don\'t) stay organized': (
        "Staying organized is tricky. Start small: use a planner, create to-do lists, and set reminders for tasks."
    ),
    r'i (forget | have problems with remambering) things': (
        "Forgetting happens to everyone, especially with ADHD. Use tools like alarms, sticky notes, or apps to track important tasks."
    ),
    r'i procrastinate': (
        "Procrastination can be a challenge. Break tasks into smaller steps, and reward yourself after completing each one."
    ),
    r'i feel overwhelmed': (
        "Feeling overwhelmed is normal. Prioritize tasks, and take things one step at a time. It's okay to ask for help."
    ),
    r'i (feel|am) anxious': (
        "Anxiety can be common with ADHD. Deep breathing, mindfulness exercises, or physical activity might help calm your mind."
    ),

    # Productivity and Lifestyle Tips
    r'how can i be more productive': (
        "To boost productivity, try using time-blocking techniques and minimize distractions by creating a quiet workspace."
    ),
    r'how can i manage my time': (
        "Time management is key. Use a calendar or time-tracking app, and try tackling the hardest tasks early in the day."
    ),
    r'how can i get motivated': (
        "Getting motivated can be tough. Start with a small, achievable goal, and remind yourself of the rewards for completing it."
    ),
    r'how do i deal with impulsiveness': (
        "Impulsiveness can be managed by pausing before making decisions, practicing mindfulness, and setting clear boundaries."
    ),

    # Self-Care and Mental Health
    r'how can i (relax|calm down|sleep)': (
        "To relax, try deep breathing, yoga, or a hobby you enjoy. Taking breaks and resting is just as important as being productive."
    ),
    r'how do i take care of myself': (
        "Self-care is vital! Eat balanced meals, exercise regularly, get enough sleep, and don’t hesitate to talk to a professional if needed."
    ),
    r'what should i do when i feel down': (
        "When feeling down, reach out to someone you trust, write down your thoughts, or engage in an activity that brings you joy."
    ),

    # ADHD-Specific Tools and Advice
    r'what tools can help with adhd': (
        "Apps like Todoist, Trello, or Evernote can help with organization. Noise-canceling headphones and timers are also great tools."
    ),
    r'how can i build good habits': (
        "Building habits takes time. Start small, stay consistent, and use reminders or habit-tracking apps to keep you on track."
    ),

    # Encouragement and Empathy
    r'i feel like i\'m failing': (
        "You’re not failing. Living with ADHD is challenging, but every small step you take is progress. Be kind to yourself!"
    ),
    r'(.*) nobody understands me': (
        "I hear you, and I want you to know you're not alone. Many people with ADHD feel this way. Have you tried talking to a support group or therapist?"
    ),
    r'i don\'t know where to start': (
        "Starting is often the hardest part. Pick one small thing to do, even if it feels insignificant. Progress, not perfection!"
    ),
    r'can i (.*)': (
        "Of course you can! ADHD can make things harder, but it doesn’t mean you can’t succeed. What would you like to achieve?"
    ),

    # Ending the Conversation
    r'bye|exit|quit': 'Goodbye! Remember, you’re doing your best, and that’s enough. Take care!',
    r'thank you': 'You’re welcome! I’m always here to help if you need advice or support.',
    r'(.*)': 'I’m not sure how to respond to that, but I’m here to help with ADHD-related challenges!'
}


import re

def chatbot_response(user_input):
    for pattern, response in rules.items():
        match = re.search(pattern, user_input, re.IGNORECASE)  # Case-insensitive match
        if match:
            # Check if response has placeholders
            if '{1}' in response and match.groups():
                return response.format(*match.groups())
            return response
    return "I'm not sure how to respond to that."

def chat():
    print("Chatbot: Hello! Type 'exit' or 'quit' to end the chat.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()