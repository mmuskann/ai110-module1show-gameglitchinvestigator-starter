# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game gave incorrect hints. For example, the secret number was 68 and I had guessed 50 it would tell me to go lower. The hints were backwards. Also, another thing I noticed that was broken was that it gave me a score of -65 at the end when I was unable to guess. The score should be 0 at minimun. After finishing the game I noticed a 3rd bug which was the new game button would not work. It did not reset the attempts and I had to refresh the tab in order to play the game again.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude for this project. I occusanily used ChatGpt for some of the code I didn't understand. One example of a suggestion that Claude gave which was correct is the logic behind the check_guess was broken. It simily told me it was because of the signs and later helped me write test cases. One exampleof a suggestion it gave that was incoorect or misleading was weather the attemps should start from 0 or 1. I wasn't sure either myself because they both techailly made sense in my head. I verfied it by trying both suggestions and seeing which one worked.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided weather a bug was actually by running the app and trying to check if the bug was still there by trying different inputs and testing for the bug multiple times before I was 100% sure. I am not too familar with pytest but one test I ran was checking if guess_check fuction actually worked. After doing pytest I was sure the logic was correct and that bug no longer existed. Yes, Calude helped me deign the tests and ChatGpt helped me understand those test. I didn't uderstand what assert did so I simily asked ChatGpt and it told me. I made sure I knew exactly what each line in the test was doing. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

If I am being honest, I myself am unsure exactly what Streamlit and state is even after looking it up. I am not familar with it at all and don't think I leanred much to anything about it. Since it was the first project I kind of found evertyhing confusin.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit or strategy i wanted to use it to prompting by telling the exact file I am reffering to and explain a bit better to the ai what I mean. Something I would do differently next to work with AI on a coding task is read the code fully myself, then ask it to explain it, find the bug myself and then ask ai about it. This project changed the way I think about AI generated code is that it is great. It might be even better than what I could write and had great suggetions. 
