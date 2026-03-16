# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
My answer:
When I made a guess of 50, the hint said to go lower but the secret number was 56. The “go lower” and “go higher” hints were swapped. Additionally. It did not allow me to start a new game and submit new guesses after finishing the first game. In “hard” difficulty, the range is supposed to be 1-50, but the secret number is 76. The secret number is outside the respective difficulty range. Also, regardless of which difficulty the user chooses it always says “Guess a number between 1 and 100”.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
My answer:
I used claude copilot. I used it to explain to me why those errors were happening and what was the logic the code was following that led to it making the errors.
Claude said that new game button used hardcoded random.randint(1,100) code to generate the new secret number in the 1-100 range, when it should have been choosing a number between low-high range, depending on which difficulty the user chose. All the fixes AI suggested was correct, they were not incorrect or misleading.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
My answer:
I told Claude to generate tests and check if the bugs were fixed. For instance, on even turns the variable "Secret" was cast to string and because of it it was not comparing numbers correctly, leading to wrong "go higher","go lower" outputs, claude added tests to check if it was now printing correct instructions. I also checked the website and checked if the bugs were still there on my own, as well. 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---
Everytime you interact with streamlit app, like click a button, the app refreshes, restarts from scratch. Session state is where you can store the values and information between the interactions so that it is not lost.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I will start using AI more for explaining already written code, and explaining the logic behind why a certain error has occured, and where that mistake is happening in the code. It made me realize that even if the code is AI generated, it might still have errors and mistakes that I need to find, verify, and debug. 