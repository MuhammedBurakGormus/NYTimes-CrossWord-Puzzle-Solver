# NYTimes-CrossWord-Puzzle-Solver

The purpose of the project is to find correct answers for the NY Times crossword puzzle by implementing AI. The accuracy rate is about 3/10 considering 16 test that are run at different dates and different puzzles. 

Solving a crossword puzzle is a two-step process that is generating a candidate answers list corresponding to each clue and choosing the most suitable one among them. 

In order to create a candidate answers list, the sources;
- Wordnet 
- Wikipedia 
- Word2vec 
- PyDictionary are used. 

As the second part of our project, it is needed to choose an answer among candidates. In this step, the algorithm proposed by us consists of two steps:
- Filter the words by the length of the answer
- Then implement the algorithm that uses the heuristic information is based on the number of intersections. 

--- 
In detail, the projects consists of 4 implementation steps:
1. Scraping & Parsing the Puzzle
2. Graphical User Interface (GUI)
3. Candidate Answers List Generation
4. Algorithm For Choosing The Answer

---

The screenshots of two runs are given below. In the figures, the screenshots of the GUI are taken. The left portion stands for the official answers, while the right portion demonstrates the answers that are found using AI. 

<img width="550" alt="Ekran Resmi 2021-11-29 22 38 56" src="https://user-images.githubusercontent.com/77242876/143931727-1cb3cba7-423c-4aab-9832-8e16bc4e51c6.png">
Figure 1 (with an accuracy rate of 0.5)

<img width="549" alt="Ekran Resmi 2021-11-29 22 39 34" src="https://user-images.githubusercontent.com/77242876/143931744-1fd4fd64-9154-4644-a6dd-df4ec9b4df63.png">
Figure 2 (with an accuracy rate of 0.2)

---

# Future Work
In the project, it is observed that the correct answers are mostly in the candidate lists. However, the selection algorithm that is based on the number of intersection letters is likely to eliminate the correct answers, and rather give a faulty answer. Then, it is clear that the algorithm needs an improvement. Therefore, combining the proposed algorithm with the AC3 algorithm could be beneficial for the sake of the project.


